from django.db import models
from datetime import date

class Estudante:
    def __init__(self, nome: str, matricula: str, curso: str):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso


class Empresa:
    def __init__(self, nome: str, cnpj: str):
        self.nome = nome
        self.cnpj = cnpj


class ProfessorOrientador:
    def __init__(self, nome: str):
        self.nome = nome


class SupervisorEmpresa:
    def __init__(self, nome: str):
        self.nome = nome


class Estagio:
    def __init__(self, tipo: str, carga_horaria: int, status: str):
        self.tipo = tipo
        self.carga_horaria = carga_horaria
        self.status = status


class Relatorio:
    def __init__(self, data_envio: date, status: str):
        self.data_envio = data_envio
        self.status = status



#class Produto(models.Model):
#    nome = models.CharField(max_length=100)
#    preco = models.DecimalField(max_digits=6, decimal_places=2)
#    descricao = models.TextField()
#    disponivel = models.BooleanField(default=True)
#
#    def __str__(self):
#        return self.nome