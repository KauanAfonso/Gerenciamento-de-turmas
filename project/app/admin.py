from django.contrib import admin
from .models import Professor, Turma, Turma_Professor, Horario

# Register your models here.
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Turma_Professor)
admin.site.register(Horario)