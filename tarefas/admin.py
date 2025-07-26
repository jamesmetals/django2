from django.contrib import admin
from .models import Tarefa  

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'criado_em', 'concluida')

admin.site.register(Tarefa, TarefaAdmin)    
