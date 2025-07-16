from django.contrib import admin
from django.urls import path
from tarefas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("tarefas/", views.home, name="home")
]

