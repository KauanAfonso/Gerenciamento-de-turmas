from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class usuariosDoSistema(UserAdmin):
    list_display = ('username', 'email', 'ra', 'data_nascimento', 'foto_perfil', 'pk_turma', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        (None, {  # Título para a nova seção no Django Admin
            "fields": ('ra', 'data_nascimento', 'foto_perfil', 'pk_turma'),
        }),
    )

    # Quando for criar um usuário novo, aparecer isso daqui
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": ('ra', 'data_nascimento', 'foto_perfil', 'pk_turma'),
        }),
    )

    
# Register your models here.
admin.site.register(Aulas)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Materia)
admin.site.register(Dias_semanas_Aulas)
admin.site.register(Dias_semanas)
admin.site.register(Horario)
admin.site.register(Aluno,usuariosDoSistema)