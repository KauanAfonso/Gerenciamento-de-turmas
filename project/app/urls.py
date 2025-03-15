
from django.urls import path
from . import views

urlpatterns = [
    path("turmas/", views.mostrar_turmas , name='mostrar_turmas'),
    path("turmas/detalhes/<int:pk>", views.visualizar_sala , name='detalhes_turmas'),
]