from django.db import models
from django.contrib.auth.models import User


# Modelo responsável por armazenar conteúdos de áudio e vídeo da plataforma
class Content(models.Model):
    # Tipos de conteúdo suportados
    CONTENT_TYPES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    # Estados possíveis de um conteúdo
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
        ('archived', 'Archived'),
    ]

    # Título do conteúdo
    title = models.CharField(max_length=255)

    # Descrição detalhada do conteúdo
    description = models.TextField()

    # URL do arquivo principal
    file_url = models.URLField()

    # URL da miniatura do conteúdo
    thumbnail_url = models.URLField(blank=True, null=True)

    # Tipo do conteúdo (áudio ou vídeo)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)

    # Data de envio do conteúdo
    upload_date = models.DateTimeField(auto_now_add=True)

    # Quantidade de visualizações
    views = models.IntegerField(default=0)

    # Quantidade de curtidas
    likes = models.IntegerField(default=0)

    # Define se o conteúdo é público
    is_public = models.BooleanField(default=True)

    # Status atual do conteúdo
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published')

    # Usuário responsável pela criação do conteúdo
    creator = models.ForeignKey(User, related_name='contents', on_delete=models.CASCADE)

    # Retorna o título como representação textual
    def __str__(self):
        return self.title
    
   


# Modelo responsável pelo agrupamento de conteúdos em playlists
class Playlist(models.Model):
    title = models.CharField(max_length=255)  # Título da playlist
    description = models.TextField(blank=True, null=True)  # Descrição opcional
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')  # Proprietário
    contents = models.ManyToManyField(Content, related_name='playlists', blank=True)  # Conteúdos (N:N)
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    updated_at = models.DateTimeField(auto_now=True)  # Data de última atualização

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    # Retorna o título da playlist
    def __str__(self):
        return self.title


# Modelo que representa um estudante
class Estudante(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=255)

    class Meta:
        ordering = ['nome']

    # Retorna o nome do estudante
    def __str__(self):
        return self.nome


# Modelo que representa uma empresa
class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)

    class Meta:
        ordering = ['nome']

    # Retorna o nome da empresa
    def __str__(self):
        return self.nome


# Modelo que representa o professor orientador do estágio
class ProfessorOrientador(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        ordering = ['nome']

    # Retorna o nome do professor orientador
    def __str__(self):
        return self.nome


# Modelo que representa o supervisor vinculado à empresa
class SupervisorEmpresa(models.Model):
    nome = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, related_name='supervisores', on_delete=models.CASCADE)

    class Meta:
        ordering = ['nome']

    # Retorna o nome do supervisor
    def __str__(self):
        return self.nome


# Modelo responsável por armazenar informações de estágio
class Estagio(models.Model):
    # Tipos de estágio disponíveis
    TIPO_CHOICES = [
        ('obrigatorio', 'Obrigatório'),
        ('nao_obrigatorio', 'Não Obrigatório'),
    ]

    # Situações possíveis do estágio
    STATUS_CHOICES = [
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    carga_horaria = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em_andamento')
    estudante = models.ForeignKey(Estudante, related_name='estagios', on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, related_name='estagios', on_delete=models.CASCADE)
    professor_orientador = models.ForeignKey(ProfessorOrientador, related_name='estagios', on_delete=models.CASCADE)
    supervisor_empresa = models.ForeignKey(SupervisorEmpresa, related_name='estagios', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    # Representação textual do estágio
    def __str__(self):
        return f"Estágio de {self.estudante} em {self.empresa}"


# Modelo responsável pelo armazenamento de relatórios de estágio
class Relatorio(models.Model):
    # Situações possíveis do relatório
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    ]

    data_envio = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    estagio = models.ForeignKey(Estagio, related_name='relatorios', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_envio']

    # Representação textual do relatório
    def __str__(self):
        return f"Relatório de {self.estagio} ({self.data_envio})"