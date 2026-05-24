from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarefa

def lista_tarefas(request):
  tarefas = Tarefa.objects.all()
  return render(request, "tarefas/lista.html", 
                {"tarefas": tarefas})

# criar 
def criar_tarefa(request):
  if request.method == "POST":
    Tarefa.objects.create(
      nome=request.POST["nome"],
      descricao=request.POST["descricao"],
      data_criacao=request.POST["data_criacao"],
      status=request.POST["status"]     
    )
    return redirect("lista_tarefas")
  return render(request, "tarefas/form_tarefa.html")

# editar
def editar_tarefa(request, id):
  tarefa = get_object_or_404(Tarefa, id=id)

  if request.method == "POST":
    tarefa.nome = request.POST["nome"]
    tarefa.descricao = request.POST["descricao"]
    tarefa.data_criacao = request.POST["data_criacao"]
    tarefa.status = request.POST["status"]
    tarefa.save()
    return redirect("lista_tarefas")
  return render(request, "tarefas/form_tarefa.html", {"tarefa": tarefa})

# deletar
def deletar_tarefa(request, id):
  tarefa = get_object_or_404(Tarefa, id=id)
  tarefa.delete()
  return redirect("lista_tarefas")  