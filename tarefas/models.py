from django.db import models

class Tarefa(models.Model):
  STATUS_CHOICES = [
    ("pendente", "Pendente"),
    ("em_andamento", "Em andamento"),
    ("bloqueado", "Bloqueado"),
    ("concluida", "Concluída"),
  ]

  nome = models.CharField(max_length=100)
  descricao = models.TextField()
  data_criacao = models.DateField()
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente")

  def __str__(self):
    return self.nome