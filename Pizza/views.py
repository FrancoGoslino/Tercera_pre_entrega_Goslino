from django.shortcuts import render
from Pizza.models import Bebida, Pizza, Empanada
from Pizza.forms import BebidaForm, PizzaForm, EmpanadaForm
def BASE(request):
    return render(request, "Pizza/BASE.html")
#-----------FUNCION BEBIDA-------->
def agregar_bebida(request):
    if request.method == 'POST':
        form = BebidaForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            bebida = Bebida(
                nombre_bebida=data.get('nombre_bebida'),
                precio_bebida=data.get('precio_bebida'),
                marca_bebida= data.get('marca_bebida'),
                litros_bebida= data.get('litros_bebida'),
            )
            bebida.save()
            return render(request, 'Pizza/bebida.html', )
        else:
            return render(request, 'Pizza/bebida.html', {'form': form})
    form_bebida = BebidaForm()
    return render(request, 'Pizza/bebida.html', {'form': form_bebida})
"""context = {
         "bebidas": Bebida.objects.all(),
         "form": BebidaForm(),
         }
    return render(request, "Pizza/bebida.html", context)   
"""
        #-----------FUNCION BUSCAR BEBIDAS-------->
def buscar_bebida(request):
    opcion=request.GET.get('opcion')
    context= {"bebidas":Bebida.objects.filter(nombre_bebida__icontains=opcion).all()}    
    return render(request, 'Pizza/bebida.html', context)
        #-----------FUNCION BUSCAR BEBIDAS-------->
def mostrar_bebida(request):
    context = {
         "bebidas": Bebida.objects.all(),
         "form": BebidaForm(),
         }
    return render(request, "Pizza/BASE.html", context)            

def mostrar_otro(request):
    bebidas=Bebida.objects.all()
    return render(request,'Pizza/BASE.html', {"bebidas": bebidas})

#-----------FUNCION PIZZA-------->
def agregar_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
    
            pizza = Pizza(
                nombre_Pizza=data.get('nombre_Pizza'),
                precio_Pizza=data.get('precio_Pizza'),
                descripcion_Pizza= data.get('descripcion_Pizza'),
                tamanio_Pizza= data.get('tamanio_Pizza'),
            )
            pizza.save()
        else:
            return render(request, 'Pizza/pizza.html', {'form': form})
    form_pizza= PizzaForm()
    return render(request, 'Pizza/pizza.html', {'form': form_pizza})


#-----------FUNCION EMPANADUQUIS-------->
def agregar_empanada(request):
    if request.method == 'POST':
        form = EmpanadaForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
    
            empanada = Empanada(
                nombre_empanada=data.get('nombre_empanada'),
                precio_empanada=data.get('precio_empanada'),
                coccion_empanada= data.get('tipo_de_coccion_de_empanada'),
                sabor_empanada= data.get('sabor_empanada'),
            )
            empanada.save()
        else:
            return render(request, 'Pizza/empanada.html', {'form': form})
    form_empanada= EmpanadaForm()
    return render(request, 'Pizza/empanada.html', {'form': form_empanada})







def buscar_bebida(request):
    opcion=request.GET.get('opcion')
    context= {"bebidas":Bebida.objects.filter(nombre_bebida__icontains=opcion).all()}    
    return render(request, 'Pizza/bebida.html', context)




def buscar (request):
       nombre = request.GET.get('nombre')
       cliente= Bebida.objects.filter(nombre_bebida__icontains=nombre)

       return render(request, "Pizza/resultado_busqueda.html", {"cliente":cliente, "nombre":nombre})
   
   
   
def busquedaBebida (request):
    return render (request, "Pizza/busqueda_bebida.html")