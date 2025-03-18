from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from django.http import HttpResponseNotFound
from .forms import *

# Create your views here.


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



''''

-----------------------------------PARTE DO ADMINISTRADOR----------------------------

'''

def criar_aula(request,pk):
    try:
        if request.method == 'POST':
            formulario = AulasForm(request.POST)

            if formulario.is_valid():
                formulario.save()
                return redirect("detalhes.html") 
                
        else:
            formulario = AulasForm(initial={'pk_turma':pk})
        return render(request, 'form_aula.html', {'form':formulario, "mensagem":"Criar essa aula?"})
    except Exception as e:
        print('erro' + e)
        return HttpResponseNotFound("Erro ao tentar criar aula.")            


def deletar_aula(request, pk):
    try:
        aula = get_object_or_404(Aulas,pk=pk)

        if request.method == "POST":
            aula.delete()
            return redirect("mostrar_turmas")
        else:
            return render(request, "excluir_aula.html", {"aula":aula})
    except Exception as e:
        print("ERRO" + e)
        return HttpResponseNotFound("Erro ao tetnar deletar a aula.")  


def atualizar_aula(request,pk):
    try:
        aula = get_object_or_404(Aulas, pk=pk)
        if request.method == 'POST':
            formulario = AulasForm(request.POST, instance=aula)

            if formulario.is_valid():
                formulario.save()
                return redirect("detalhes.html") 
                
        else:
            formulario = AulasForm(instance=aula)
        return render(request, 'form_aula.html', {'form':formulario, "mensagem":"Atualizar essa aula?"})
    except Exception as e:
        print("Erro" + e)
        return HttpResponseNotFound("Erro ao tentar atulizar a aula")     