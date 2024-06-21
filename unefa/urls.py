from django.urls import path

#AQUI SE ESTA IMPORTANDO EL ARCHIVO VIEWS.PY QUE ESTA EN LA CARPETA
from . import views

urlpatterns = [
    path('answer/', views.answer, name='answer'),
]