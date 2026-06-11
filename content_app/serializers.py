from rest_framework import serializers

from .models import (
    Content,
    Empresa,
    Estagio,
    Estudante,
    Playlist,
    ProfessorOrientador,
    Relatorio,
    SupervisorEmpresa,
)


# Serializer responsável pela conversão de conteúdos para JSON
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

        # Métricas e metadados não devem ser graváveis pelo cliente.
        read_only_fields = ['views', 'likes', 'upload_date', 'creator']


# Serializer responsável pelas playlists
class PlaylistSerializer(serializers.ModelSerializer):
    # Leitura: conteúdos serializados de forma detalhada
    contents = ContentSerializer(many=True, read_only=True)

    # Escrita: lista de IDs de conteúdos
    content_ids = serializers.PrimaryKeyRelatedField(
        queryset=Content.objects.all(), write_only=True, many=True, source='contents'
    )

    class Meta:
        model = Playlist
        fields = ['id', 'title', 'description', 'user', 'contents', 'content_ids', 'created_at']
        read_only_fields = ['user', 'created_at']

    # Cria uma playlist associando os conteúdos informados
    def create(self, validated_data):
        content_data = validated_data.pop('contents', [])
        playlist = super().create(validated_data)
        playlist.contents.set(content_data)
        return playlist

    # Atualiza uma playlist e seus conteúdos relacionados
    def update(self, instance, validated_data):
        content_data = validated_data.pop('contents', None)
        playlist = super().update(instance, validated_data)
        if content_data is not None:
            playlist.contents.set(content_data)
        return playlist


# Serializer responsável pelos estudantes
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'matricula', 'curso']

    # Valida o campo matrícula
    def validate_matricula(self, value):
        if not value.strip():
            raise serializers.ValidationError('A matrícula não pode ser vazia.')
        return value


# Serializer responsável pelas empresas
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'nome', 'cnpj']

    # Validação básica do CNPJ
    def validate_cnpj(self, value):
        # Remove máscara e valida que sobram 14 dígitos.
        digitos = ''.join(filter(str.isdigit, value))
        if len(digitos) != 14:
            raise serializers.ValidationError('CNPJ deve conter 14 dígitos.')
        return value


# Serializer responsável pelos professores orientadores
class ProfessorOrientadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorOrientador
        fields = ['id', 'nome']


# Serializer responsável pelos supervisores das empresas
class SupervisorEmpresaSerializer(serializers.ModelSerializer):
    # Exibe o nome da empresa vinculada ao supervisor
    empresa_nome = serializers.CharField(source='empresa.nome', read_only=True)

    class Meta:
        model = SupervisorEmpresa
        fields = ['id', 'nome', 'empresa', 'empresa_nome']


# Serializer responsável pelos estágios
class EstagioSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.CharField(source='estudante.nome', read_only=True)
    empresa_nome = serializers.CharField(source='empresa.nome', read_only=True)

    class Meta:
        model = Estagio
        fields = [
            'id',
            'tipo',
            'carga_horaria',
            'status',
            'estudante',
            'estudante_nome',
            'empresa',
            'empresa_nome',
            'professor_orientador',
            'supervisor_empresa',
        ]

    # Valida a carga horária do estágio
    def validate_carga_horaria(self, value):
        if value <= 0:
            raise serializers.ValidationError('A carga horária deve ser maior que zero.')
        return value

    # Garante consistência entre empresa e supervisor selecionados
    def validate(self, attrs):
        # O supervisor deve pertencer à empresa do estágio.
        empresa = attrs.get('empresa') or getattr(self.instance, 'empresa', None)
        supervisor = attrs.get('supervisor_empresa') or getattr(self.instance, 'supervisor_empresa', None)

        if empresa and supervisor and supervisor.empresa_id != empresa.id:
            raise serializers.ValidationError(
                {'supervisor_empresa': 'O supervisor deve pertencer à empresa selecionada.'}
            )

        return attrs


# Serializer responsável pelos relatórios de estágio
class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = ['id', 'data_envio', 'status', 'estagio']