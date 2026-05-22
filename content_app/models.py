from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    CONTENT_TYPES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='published')
    creator = models.ForeignKey(User, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
   


class Estudante(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome


class ProfessorOrientador(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class SupervisorEmpresa(models.Model):
    nome = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, related_name='supervisores', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Estagio(models.Model):
    TIPO_CHOICES = [
        ('obrigatorio', 'Obrigatório'),
        ('nao_obrigatorio', 'Não Obrigatório'),
    ]

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

    def __str__(self):
        return f"Estágio de {self.estudante} em {self.empresa}"


class Relatorio(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    ]

    data_envio = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    estagio = models.ForeignKey(Estagio, related_name='relatorios', on_delete=models.CASCADE)

    def __str__(self):
        return f"Relatório de {self.estagio} ({self.data_envio})"