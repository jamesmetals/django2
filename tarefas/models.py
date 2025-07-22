from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
