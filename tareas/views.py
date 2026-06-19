from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .forms import TareaForm

# Funcion auxiliar para comprobar si el usuario es admin

def es_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required # si no está logueado, lo redirige al login

def dashboard(request):
    # pasamos el usuario logueado al HTML
    return render(request, 'dashboard.html', {'usuario': request.user})

@login_required
@user_passes_test(es_admin) # Solo pasa si la funcion es_admin devuelve True

def crear_proyecto(request):
    return HttpResponse("Bienvenido Admin. Aquí podrás crear proyectos)")

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        # El usuario hizo click en guardar tarea
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save() # Guarda la tarea en la base de datos
            return redirect('dashboard') # Redirige al dashboard después de guardar
    else:
        form = TareaForm()
        
    return render(request, 'crear_tarea.html', {'form': form})