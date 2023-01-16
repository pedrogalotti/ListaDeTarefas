from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('home/', views.home, name="home"),
    path('criar_tarefa/', views.criar_tarefa, name="criar_tarefa"),
    path('ver_tarefa/<int:id>', views.ver_tarefa, name="ver_tarefa"),
    path('editar_tarefa/<int:id>', views.editar_tarefa, name="editar_tarefa"),
    path('concluir_tarefa/<int:id>', views.concluir_tarefa, name="concluir_tarefa"),
    path('excluir_tarefa/<int:id>', views.excluir_tarefa, name="excluir_tarefa"),
]