from django import forms
from .models import *


class ProfessorForm(forms.Form):
    class meta:
        model = Professor
        fields = '__all__'

class turmasForm(forms.Form):
    class meta:
        model = Turma
        fields = '__all__'
