from django.shortcuts import render
from .forms import TarefaForm
from django.shortcuts import redirect
frase=("Adiciionar")

def home(request):
    return render(request, 'tarefas/home.html')

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
