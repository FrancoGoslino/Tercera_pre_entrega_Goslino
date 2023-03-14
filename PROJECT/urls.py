"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pizza.views import BASE, agregar_bebida, agregar_pizza ,agregar_empanada, buscar_bebida, mostrar_bebida, mostrar_otro

urlpatterns = [
    path('', BASE, name="BASE"),
    path('admin/', admin.site.urls),
    path('agregar/bebida/',agregar_bebida, name="agregar/bebida/" ),
    path('agregar/pizza/', agregar_pizza, name= 'agregar/pizza/'),
    path('agregar/empanada/', agregar_empanada, name='agregar/empanada/'),
    path('buscar/bebida/', buscar_bebida, name= 'buscar/bebida/'),
    path('mostrar/bebida/', mostrar_bebida, name='mostrar/bebida/'),
    path('mostrar/otro/', mostrar_otro, name= 'mostrar/otro/')
]
    
    
    
    
    
    
    