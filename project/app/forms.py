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

        labels = {
            'serie_turma':"Chose class series"
        }

        

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        pk_turma = forms.IntegerField(label='aa', required=False)  # Adicionando o campo dentro da classe meta para que o valor padrão ja apareça la
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'ra', 'data_nascimento',  'pk_turma', 'foto_perfil', 'is_active']

        labels = {
            'username': 'Nome de Usuário',
            'password':"Senha",
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
        
        def save(self, commit=True):
            user = super().save(commit=False)
        
        # Se uma nova senha for fornecida, criptografa ela
            if self.cleaned_data.get('password'):
                user.password = make_password(self.cleaned_data['password'])
        
            if commit:
                user.save()
            return user

class AulasForm(forms.ModelForm):
   
    class Meta:
        model = Aulas
        pk_turma = forms.IntegerField(label='aa', required=False)  # Adicionando o campo dentro da classe meta para que o valor padrão ja apareça la
        fields = '__all__'

        labels = {
            'pk_professor': 'Chose a teacher:',
            'pk_turma': 'Chose a classroom:',
            'pk_materia': 'Chose a subject:',
            'pk_horario': 'Chose a class time:',
            'pk_dias_semana': "Chose a week's day:"
        }

