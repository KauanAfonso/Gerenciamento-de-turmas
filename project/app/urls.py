
from django.urls import path
from . import views

urlpatterns = [
    path("turmas/", views.mostrar_turmas , name='mostrar_turmas')
]