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
        pk_turma = forms.IntegerField(label='aa', required=False)  # Adicionando o campo dentro da classe meta para que o valor padrão ja apareça la
        fields = '__all__'
