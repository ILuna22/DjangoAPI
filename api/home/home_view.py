from django.shortcuts import render
# Importa la función `render` del módulo `shortcuts` de Django, 
# que facilita la renderización de plantillas HTML en las vistas.

# Create your views here.
# Comentario por defecto de Django que indica que este archivo es donde se definen las vistas.

def home_views(request):
    # Define una vista llamada `login_view` que toma el argumento `request`. 
    # `request` es un objeto que contiene todos los datos asociados con la solicitud HTTP.

    template_view = "index.html"
    # Asigna el nombre de la plantilla que queremos renderizar, en este caso "login.html". 
    # `template_name` es una variable que hace referencia a la ubicación del archivo HTML.

    return render(request, template_name=template_view)
    # La función `render` genera una respuesta HTTP que contiene el contenido de la plantilla HTML.
    # Toma dos argumentos principales:
    # 1. `request`: El objeto de solicitud.
    # 2. `template_name`: El nombre de la plantilla a renderizar.
    # Esta función devuelve una respuesta con la plantilla procesada.
