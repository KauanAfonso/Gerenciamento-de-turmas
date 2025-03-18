from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from django.http import HttpResponseNotFound
from .forms import *
from django.contrib import messages



''''

-----------------------------------PARTE DO ADMINISTRADOR----------------------------

Aqui serão as ações do administrador


'''

def criar_aula(request,pk):
    try:
        if request.method == 'POST':
            formulario = AulasForm(request.POST)

            if formulario.is_valid():
                formulario.save()
                return redirect("mostrar_turmas") 
                
        else:
            formulario = AulasForm(initial={'pk_turma':pk})
        return render(request, 'form_aula.html', {'form':formulario, "mensagem":"Criar essa aula?"})
    except Exception as e:
        print('erro' , e)
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
        print("ERRO" , e)
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
        print("Erro" , e)
        return HttpResponseNotFound("Erro ao tentar atulizar a aula")     
    


#Turma

def criar_turma(request):
    try:
        if request.method == 'POST':
            formulario = TurmasForm(request.POST)

            if formulario.is_valid():
                formulario.save()
                return redirect("mostrar_turmas") 
                
        else:
            formulario = TurmasForm()
        return render(request, 'form_aula.html', {'form':formulario, "mensagem":"Criar essa turma?"})
    except Exception as e:
        print('erro' , e)
        return HttpResponseNotFound("Erro ao tentar criar turma.")
    
def atualizar_turma(request,pk):
    try:
        turma = get_object_or_404(Turma, pk=pk)
        if request.method == "POST":
            formulario = TurmasForm(request.POST, instance=turma) #cirando um form com instaancia de um id especifico
            if formulario.is_valid():
                formulario.save()
                return redirect('mostrar_turmas')
            else:
                messages.error(request, "Erro ao tentar atualizar a turma. Verifique os dados e tente novamente.")
                return render(request, 'form_aula.html', {'form': formulario, "mensagem": "Atualizar essa turma?"})
        else:
            formulario = TurmasForm(instance=turma)
            return render(request, 'form_aula.html', {'form':formulario, "mensagem":"Atualizar essa sala?"})
    except Exception as e:
        print('erro: ' , e)
        return HttpResponseNotFound("Erro ao tentar atualizar a turma")


def excluir_turma(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    try:
        formulario = TurmasForm(request.POST, instance=turma)
        if formulario.is_valid():
            turma.delete()
            return redirect('mostrar_turmas')
        else:
            formulario = TurmasForm(instance=turma)
            return render(request, 'form_aula.html', {'form':formulario, "mensagem":"Deseja excluir essa sala?"})
    except Exception as e:
        print('erro: ' , e)
        return HttpResponseNotFound("Erro ao tentar excluir a turma" )