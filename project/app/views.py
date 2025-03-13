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
    

def ver_professor_turma(request, pk):
    try:
        id_turma = get_object_or_404(Turma, pk=pk)
        turma_professores = Turma_Professor.objects.filter(turma=id_turma)
        
        professores_materias = []

        for tp in turma_professores:
            professores_materias.append({
                'professor': tp.professor,
                'materia': tp.materia,
                'horario': tp.horario,
            })

        return render(request, "detalhes.html", {"turma": id_turma, "professores": professores_materias})
    except Exception as e:
        print(f"Error: {e}")
        
        # Return a 404 response with a custom error message
        return HttpResponseNotFound("Ocorreu um erro ao tentar carregar a turma e os professores.")


