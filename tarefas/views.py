from django.shortcuts import render
from django.http import HttpResponse

frase=("Adiciionar")

def home(request):
    return render(request, 'tarefas/home.html')

def add(request):
    # Logic for adding a task would go here
    return HttpResponse (frase)

def adicionar(request):
    return render(request, 'adicionar/home.html')