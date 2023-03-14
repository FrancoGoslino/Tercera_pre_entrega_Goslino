from django.shortcuts import render
from Pizza.models import Bebida, Pizza, Empanada
from Pizza.forms import BebidaForm, PizzaForm, EmpanadaForm


def BASE(request):
    return render(request, "Pizza/BASE.html")
#-------------------------------------------------------------------------------------------------------------------#
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


        #-----------FUNCION BUSCAR BEBIDAS-------->
def buscar_bebida(request):
    if request.GET["nombre_bebida"]: 
        opcion=request.GET.get('nombre_bebida')
        context= {"bebidas":Bebida.objects.filter(nombre_bebida__icontains=opcion).all()}    # Este nombre que asignamos, sera utilizado en bebida.html en {%  for bebida in bebidas %}
    return render(request, 'Pizza/bebida.html', context)

        #-----------FUNCIOnes de prueba BEBIDAS-------->
def mostrar_bebida(request):
    context = {
         "bebidas": Bebida.objects.all(),
         "form": BebidaForm(),
         }
    return render(request, "Pizza/BASE.html", context)            

def mostrar_otro(request):
    bebidas=Bebida.objects.all()
    return render(request,'Pizza/BASE.html', {"bebidas": bebidas})

def buscar (request):
       nombre = request.GET.get('nombre')
       cliente= Bebida.objects.filter(nombre_bebida__icontains=nombre)

       return render(request, "Pizza/resultado_busqueda.html", {"cliente":cliente, "nombre":nombre})
   
def busquedaBebida (request):
    return render (request, "Pizza/busqueda_bebida.html")

#-------------------------------------------------------------------------------------------------------------------#
#-----------FUNCION PIZZA-------->
def agregar_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
    
            pizza = Pizza(
                nombre_pizza=data.get('nombre_pizza'),
                precio_pizza=data.get('precio_pizza'),
                descripcion_pizza= data.get('descripcion_pizza'),
                tamanio_pizza= data.get('tamanio_pizza'),
            )
            pizza.save()
            return render(request, 'Pizza/pizza.html', )
        else:
            return render(request, 'Pizza/pizza.html', {'form': form})
    form_pizza= PizzaForm()
    return render(request, 'Pizza/pizza.html', {'form': form_pizza})
  
def buscar_pizza(request):
    if request.GET["nombre_pizza"]: 
        opcion=request.GET.get('nombre_pizza')
        context= {"pizzas":Pizza.objects.filter(nombre_pizza__icontains=opcion).all()}    # Este nombre que asignamos, sera utilizado en bebida.html en {%  for bebida in bebidas %}
    return render(request, 'Pizza/pizza.html', context)


#-------------------------------------------------------------------------------------------------------------------#
#-----------FUNCION EMPANADUQUIS-------->
def agregar_empanada(request):
    if request.method == 'POST':
        form = EmpanadaForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
    
            empanada = Empanada(
                nombre_empanada=data.get('nombre_empanada'),
                precio_empanada=data.get('precio_empanada'),
                coccion_empanada= data.get('coccion_empanada'),
                sabor_empanada= data.get('sabor_empanada'),
            )
            empanada.save()
            return render(request, 'Pizza/empanada.html', )
        else:
            return render(request, 'Pizza/empanada.html', {'form': form})
    form_empanada= EmpanadaForm()
    return render(request, 'Pizza/empanada.html', {'form': form_empanada})




def buscar_empanada(request):
    if request.GET["nombre_empanada"]: 
        opcion=request.GET.get('nombre_empanada')
        context= {"empanadas":Empanada.objects.filter(nombre_empanada__icontains=opcion).all()}    # Este nombre que asignamos, sera utilizado en bebida.html en {%  for bebida in bebidas %}
    return render(request, 'Pizza/empanada.html', context)



