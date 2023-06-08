
from django.db import models

class Presenca(models.Model):
    nome_aluno = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)

