from django.shortcuts import render

def home(request):
    return render(request, 'tarefas/home.html')

def add(request):
    # Logic for adding a task would go here
    return render(request, 'tarefas/add.html')  # Assuming you have an add.html template