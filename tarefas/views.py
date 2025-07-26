from django.shortcuts import render
from .forms import TarefaForm

frase=("Adiciionar")

def home(request):
    return render(request, 'tarefas/home.html')

def adicionar(request):
    form = TarefaForm()
    return render(request, 'tarefas/adicionar.html', {'form': form})

#def adicionar(request):
 # return render(request, 'adicionar/home.html')