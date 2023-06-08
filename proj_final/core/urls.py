from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_aluno, name='cadastrar_presenca'),
    path('listar_presencas/', views.listar_alunos, name='listar_presencas'),
]