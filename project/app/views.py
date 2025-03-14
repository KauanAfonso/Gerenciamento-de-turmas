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
        turma = get_object_or_404(Turma, pk=pk)
        professores = Aulas.objects.filter(pk_turma = turma)
        professores_materias = []

        for i in professores:
            print(i)
            professores_materias.append({
                'professor': i.pk_professor,
                'materia': i.pk_materia,
                'horario': i.pk_horario,
                'turma': i.pk_turma,
                'dia_semana': i.pk_dias_semana
            })

        print(professores)
        return render(request, "detalhes.html", {"turma": turma, "professores": professores_materias})
    except Exception as e:
        print(f"Error: {e}")
        
        # Return a 404 response with a custom error message
        return HttpResponseNotFound("Ocorreu um erro ao tentar carregar a turma e os professores.")


