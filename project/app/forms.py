from django import forms
from .models import Professor, Turma, Aluno, Aulas

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class TurmasForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class AulasForm(forms.ModelForm):
    class Meta:
        model = Aulas
        fields = '__all__'
