from django.shortcuts import render,redirect , get_list_or_404
from .models import *

# Create your views here.


def mostrar_turmas(request):
    try:
        turma = Turma.objects.all()
    except:
        return "erro"
    return render(request, "turmas.html" , {"turmas": turma})
    

def ver_professor_turma(request, pk):
    try:
        id_turma = get_list_or_404(Turma, pk=pk)
    except:
        return "O"


