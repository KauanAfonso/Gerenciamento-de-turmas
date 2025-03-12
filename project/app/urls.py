
from django.urls import path
from . import views

urlpatterns = [
    path("turmas/", views.mostrar_turmas , name='mostrar_turmas'),
    path("turmas/detalhes/<int:pk>", views.ver_professor_turma , name='detalhes_turmas'),
]