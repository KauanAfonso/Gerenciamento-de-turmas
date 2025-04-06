
from django.urls import path
from . import adm
from . import views


urlpatterns = [
    path("turmas/", views.mostrar_turmas , name='mostrar_turmas'),
    path("turmas/detalhes/<int:pk>", views.visualizar_sala , name='detalhes_turmas'),
    path("professores/", views.mostrar_professores, name='mostrar_professores'),
    path("professores/detalhes/<int:pk>", views.visualizar_turmas_professor, name='visualizar_turmas_professor'),
    path('turmas/detalhes/criar_aula/<int:pk>', adm.criar_aula, name='criar_aula'),
    path("deletar/<int:pk>", adm.deletar_aula, name='deletar_aula'),
    path('atualizar/<int:pk>', adm.atualizar_aula, name="atualizar_aula"),
    path("turmas/criar_turma/", adm.criar_turma, name="criar_turma"),
    path("turmas/atualizar/<int:pk>", adm.atualizar_turma, name='atualizar_turma'),
    path('turmas/deletar/<int:pk>' , adm.excluir_turma, name='excluir_turma'),
    path("turmas/criar_aluno/<int:pk>", adm.criar_aluno, name='criar_aluno'),
    path("turmas/editar_aluno/<int:pk>", adm.atualizar_aluno, name='atualizar_aluno'),
    path('turmas/excluir_aluno/<int:pk>', adm.excluir_aluno, name='excluir_aluno'),
    path('', views.logar, name='login'),
    path('logout/', views.logout_view , name='logout_view'),


]