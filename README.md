# Tercera_pre_entrega_Goslino

author: Goslino franco 

# Generalidades:

El programa es una pagina web de una rotiseria. Aun en desarrollo. Se utiliza python 3.10.8, HTML5, Css, Js.

class Bebida utiliza: 
    bebida.html, def agregar_bebida, BebidaForm, def buscar_bebida, busqueda_bebida.html

Class Pizza utiliza: 
    pizza.html, def agregar_pizza, def buscar_pizza, PizzaForm

Class Empanadas utiliza: 
    empanada.html, def agregar_empanada, def buscar_empanada, EmpanadaForm


Archivos HTML que heredan de BASE.html:
    bebida.html, empanada.html, pizza.html, resultado_busqueda.html (no se utiliza)

# Datos para ingresar al /admin:
    super user:
        name: admin
        email: frangoslino@gmail.com
        password: 123

# Pasos a seguir:
    python manage.py runserver
        1- Ya dentro de la pagina web, podremos cargar datos en las tres categorias (Bebidas, Pizzas, Empanadas). Por ejemplos, cargaremos los datos (Coca, 100, Coca Cola, 2)
        2- Luego, realizaremos la busqueda de la bebida cargada por su nombre (Coca). Visualizaremos todos los resultados que contengan la palabra Coca en su nombre.
        3- Ingresamos al admin (/admin). Alli tendremos las clases. Podremos ver, modificar y eliminar los objetos añadidos en sus respectivas clases.
    Terminadas las pruebas, cerramos server (ctrl + c).