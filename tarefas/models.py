from django.db import models

class Tarefa(models.Model):
        titulo = models.CharField(max_length=100)       
        descricao = models.TextField()       
        criado_em = models.DateTimeField(auto_now_add=True)       
        concluida = models.BooleanField(default=False)      
        
        def __str__(self):
                return self.titulo  