
from django.urls import path
from . import views

urlpatterns = [
    path("turmas/", views.mostrar_turmas , name='mostrar_turmas'),
    path("turmas/detalhes/<int:pk>", views.visualizar_sala , name='detalhes_turmas'),
    path("professores/", views.mostrar_professores, name='mostrar_professores'),
    path("professores/detalhes/<int:pk>", views.visualizar_turmas_professor, name='visualizar_turmas_professor'),
    path('turmas/detalhes/criar_aula/<int:pk>/', views.criar_aula, name='criar_aula')
]