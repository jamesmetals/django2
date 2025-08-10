from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name= "home"),
    #O path abaixo tem 2 adicionar, 1 e o nome da função, o outro e o nome do link
    path("adicionar", views.adicionar, name= "adicionar"),  
    path("tarefa/<int:id>", views.tarefa, name= "tarefa"),
]