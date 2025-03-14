from django.shortcuts import render,redirect , get_object_or_404, get_list_or_404
from .models import *
from django.http import HttpResponseNotFound

# Create your views here.


def mostrar_turmas(request):
    try:
        turma = Turma.objects.all()
    except:
        return "erro"
    return render(request, "turmas.html" , {"turmas": turma})
    
'''
Função que retornará as ifnromações da tabela de aulas 
'''
def visualizar_sala(request, pk):
    try:
        turma = get_object_or_404(Turma, pk=pk) #Pegando o id da turma 
        aulas = Aulas.objects.filter(pk_turma = turma) #Mesclando as tabelas relacionadas a aulas pela FK da turma
        aulas_info = []
        alunos = Aluno.objects.filter(pk_turma = pk)

        for aula in aulas:
            aulas_info.append({
                'professor': aula.pk_professor,
                'materia': aula.pk_materia,
                'horario': aula.pk_horario,
                'turma': aula.pk_turma,
                'dia_semana': aula.pk_dias_semana
            })#retoronado os dados 

        return render(request, "detalhes.html", {"turma": turma, "aulas": aulas_info, "alunos":alunos})
    except Exception as e:
        print(f"Error: {e}")
        
        return HttpResponseNotFound("Ocorreu um erro ao tentar carregar a turma e os professores.") #mensagem de erro caso for nescessario
