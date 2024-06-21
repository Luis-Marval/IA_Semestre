from django.contrib import admin
from django.urls import path,include

#AQUI SE ESTA IMPORTANDO EL ARCHIVO VIEWS.PY QUE ESTA EN LA CARPETA
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home),
    
    path('home/', views.home, name='home'),
    
    path('login/', views.login, name='login'),
    
    path('register/', views.register, name='register'),
    
    path('index/', views.index, name='index'),
    
    path('logout/', views.logout, name='logout'),

    path("index/",include("unefa.urls"))
    
]
