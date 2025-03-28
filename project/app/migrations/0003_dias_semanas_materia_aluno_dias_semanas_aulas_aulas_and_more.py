# Generated by Django 5.1.7 on 2025-03-14 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_horario_horario_aula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dias_semanas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('SEG', 'Segunda-Feira'), ('TER', 'Terça-Feira'), ('QUA', 'Quarta-Feira'), ('QUI', 'Quinta-Feira'), ('SEX', 'Sexta-Feira')], max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_materia', models.CharField(choices=[('Matematica', 'Matemática'), ('Portugues', 'Português'), ('Historia', 'História'), ('Geografia', 'Geografia'), ('Quimica', 'Química'), ('Fisica', 'Física'), ('Biologia', 'Biologia')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=55)),
                ('pk_turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Dias_semanas_Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pk_dia_semana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dias_semanas')),
            ],
        ),
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pk_horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.horario')),
                ('pk_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.professor')),
                ('pk_turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.turma')),
                ('pk_dias_semana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dias_semanas_aulas')),
                ('pk_materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
            ],
        ),
        migrations.DeleteModel(
            name='Turma_Professor',
        ),
    ]
