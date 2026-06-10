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


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
        # Métricas e metadados não devem ser graváveis pelo cliente.
        read_only_fields = ['views', 'likes', 'upload_date', 'creator']


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

    def create(self, validated_data):
        content_data = validated_data.pop('contents', [])
        playlist = super().create(validated_data)
        playlist.contents.set(content_data)
        return playlist

    def update(self, instance, validated_data):
        content_data = validated_data.pop('contents', None)
        playlist = super().update(instance, validated_data)
        if content_data is not None:
            playlist.contents.set(content_data)
        return playlist


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'matricula', 'curso']

    def validate_matricula(self, value):
        if not value.strip():
            raise serializers.ValidationError('A matrícula não pode ser vazia.')
        return value


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'nome', 'cnpj']

    def validate_cnpj(self, value):
        # Remove máscara e valida que sobram 14 dígitos.
        digitos = ''.join(filter(str.isdigit, value))
        if len(digitos) != 14:
            raise serializers.ValidationError('CNPJ deve conter 14 dígitos.')
        return value


class ProfessorOrientadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorOrientador
        fields = ['id', 'nome']


class SupervisorEmpresaSerializer(serializers.ModelSerializer):
    empresa_nome = serializers.CharField(source='empresa.nome', read_only=True)

    class Meta:
        model = SupervisorEmpresa
        fields = ['id', 'nome', 'empresa', 'empresa_nome']


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

    def validate_carga_horaria(self, value):
        if value <= 0:
            raise serializers.ValidationError('A carga horária deve ser maior que zero.')
        return value

    def validate(self, attrs):
        # O supervisor deve pertencer à empresa do estágio.
        empresa = attrs.get('empresa') or getattr(self.instance, 'empresa', None)
        supervisor = attrs.get('supervisor_empresa') or getattr(self.instance, 'supervisor_empresa', None)
        if empresa and supervisor and supervisor.empresa_id != empresa.id:
            raise serializers.ValidationError(
                {'supervisor_empresa': 'O supervisor deve pertencer à empresa selecionada.'}
            )
        return attrs


class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = ['id', 'data_envio', 'status', 'estagio']
