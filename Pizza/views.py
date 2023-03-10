from django.shortcuts import render
from Pizza.models import Bebida
from Pizza.forms import BebidaForm

def BASE(request):
    return render(request, "Pizza/BASE.html")




def agregar_producto(request):   
    bebida_form= BebidaForm(request.POST) 
    bebida_form.save(request)
    context= {
        "Bebidas": Bebida.objects.all(),
        "form" : BebidaForm(),
    }
    
    return render(request, "Pizza/bebida.html", context)