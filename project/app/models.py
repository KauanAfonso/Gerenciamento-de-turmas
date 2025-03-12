from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    serie_turma = models.CharField(max_length=8)
    professores = models.ManyToManyField(Professor, related_name='turmas')

    def __str__(self):
        return self.serie_turma
