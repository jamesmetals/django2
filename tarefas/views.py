from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import Tarefa
frase=("Adiciionar")

def home(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/home.html', {'tarefas': tarefas})

def adicionar(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            print("Tarefa adicionada com sucesso!")
            return redirect('home')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/adicionar.html', {'form': form})

def tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    return render(request, "tarefas/tarefa.html", {'tarefa': tarefa})
    