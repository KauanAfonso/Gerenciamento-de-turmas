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
        pk_turma = forms.IntegerField(label='aa', required=False)  # Adicionando o campo dentro da classe meta para que o valor padrão ja apareça la
        fields = ['username', 'email', 'first_name', 'last_name', 'ra', 'data_nascimento',  'pk_turma', 'foto_perfil', 'is_active']

        labels = {
            'username': 'Nome de Usuário',
            'email': 'Endereço de E-mail',
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'ra': 'Número de RA',
            'data_nascimento': 'Data de Nascimento',
            'pk_turma': 'Turma',
            'foto_perfil': 'Foto de Perfil',
            'is_active': 'Ativo'
        }

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),  # Usando DateInput para o campo de data
            
        }

class AulasForm(forms.ModelForm):
   
    class Meta:
        model = Aulas
        pk_turma = forms.IntegerField(label='aa', required=False)  # Adicionando o campo dentro da classe meta para que o valor padrão ja apareça la
        fields = '__all__'
