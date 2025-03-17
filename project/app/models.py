from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    serie_turma = models.CharField(max_length=8)
    
    def __str__(self):
        return self.serie_turma
    
class Aluno(models.Model):
    nome_completo = models.CharField(max_length=55)
    pk_turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    email = models.CharField(max_length=255,default='')

    def __str__(self):
        return self.nome_completo


class Horario(models.Model):
    horarios = [
        ("7:00h", "7:00h"),
        ("7:45h", "7:45h"),
        ("8:30h", "8:30h"),
        ("9:15h", "9:15h"),
        ("10:00h", "10:00h"),
        ("10:45h", "10:45h"),
        ("11:30h", "11:30h"),
        ("12:15h", "12:15h"),
        ("13:00h", "13:00h"),
        ("13:45h", "13:45h"),
        ("14:30h", "14:30h"),
        ("15:15h", "15:15h"),
        ("16:00h", "16:00h"),
        ("16:45h", "16:45h"),
        ("17:30h", "17:30h"),
    ]
    horario_aula = models.CharField(max_length=50,choices=horarios,unique=True)

    def __str__(self):
        return self.horario_aula
    
class Materia(models.Model):
    materias = [
        ("Matematica", "Matemática"),
        ("Portugues", "Português"),
        ("Historia", "História"),
        ("Geografia", "Geografia"),
        ("Quimica", "Química"),
        ("Fisica", "Física"),
        ("Biologia", "Biologia"),
    ]
    nome_materia = models.CharField(max_length=50,choices=materias)

    def __str__(self):
        return self.nome_materia
    

class Dias_semanas(models.Model):
    dias = [
        ("SEG", "Segunda-Feira"),
        ("TER", "Terça-Feira"),
        ("QUA", "Quarta-Feira"),
        ("QUI", "Quinta-Feira"),
        ("SEX", "Sexta-Feira"),
    ]
    dia = models.CharField(max_length=55,choices=dias, unique=True)

    def __str__(self):
        return self.dia
    
class Dias_semanas_Aulas(models.Model):
    pk_dia_semana = models.ForeignKey(Dias_semanas, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk_dia_semana)

class Aulas(models.Model):

    pk_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    pk_turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    pk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    pk_horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    pk_dias_semana = models.ForeignKey(Dias_semanas_Aulas,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.pk_professor} - {self.pk_turma} - {str(self.pk_materia)} - {str(self.pk_horario)} - {str(self.pk_dias_semana)}"