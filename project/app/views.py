from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from django.http import HttpResponseNotFound, HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() #pegando o user
            login(request,user) #passe o request e o user
            return redirect('mostrar_turmas')
        else:
            print('usuário inválido')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})

def logout_view(request):
    try:
        logout(request)
    except Exception as e:
        print('erro', e)
    return redirect('login')

def mostrar_turmas(request):
    try:
        turma = Turma.objects.all()
    except Exception as e:
        print(f"erro: {e}")
        return HttpResponseNotFound('Erro ao tentar carregar os professores')
    return render(request, "turmas.html" , {"turmas": turma})


def mostrar_professores(request):
    try:
        professores = Professor.objects.all()
    except Exception as e:
        print(f"erro: {e}")
        return HttpResponseNotFound('Erro ao tentar carregar os professores')
    return render(request, 'professores.html', {'professores':professores})
    
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
                'pk':aula.pk,
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


def visualizar_turmas_professor(request, pk):
    try:
        professor = get_object_or_404(Professor,pk=pk)
        aulas = Aulas.objects.filter(pk_professor =professor)
        professor_aulas = []
        
        for aula in aulas:
            professor_aulas.append(
                {
                    'turma': aula.pk_turma,
                    'materia': aula.pk_materia,
                    'horario': aula.pk_horario,
                    'dia_semana': aula.pk_dias_semana
                }
            )
        return render(request, 'prof_detalhes.html' , {'professores':professor_aulas})
    except Exception as e:
        print(f"Error: {e}")
        return HttpResponseNotFound("Ocorreu um erro ao tentar carregar a turma e os professores.") #mensagem de erro caso for nescessario



