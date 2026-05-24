from django.urls import path
from . import views

urlpatterns = [
 path("", views.lista_tarefas, name="lista_tarefas"),
 path("criar/", views.criar_tarefa, name="criar_tarefa"),
 path("editar/<int:id>/", views.editar_tarefa, name="editar_tarefa"),
 path("deletar/<int:id>/", views.deletar_tarefa, name="deletar_tarefa"),
]