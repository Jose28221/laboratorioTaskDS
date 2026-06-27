from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .forms import TareaForm, ProyectoForm
from .models import Proyecto, Tarea


# Funcion auxiliar para comprobar si el usuario es admin

def es_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required # si no está logueado, lo redirige al login
def dashboard(request):
    # pasamos el usuario logueado al HTML
    es_admin = request.user.is_superuser or request.user.groups.filter(name='Admin').exists()
    tareas = Tarea.objects.filter(asignada_a=request.user)
    return render(request, 'dashboard.html', 
                  {'usuario': request.user,
                   'es_admin': es_admin,
                   'tareas': tareas})

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        # El usuario hizo click en guardar proyecto
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el proyecto en la base de datos
            return redirect('dashboard') # Redirige al dashboard después de guardar
    else:
        form = ProyectoForm()        
    return render(request, 'crear_proyecto.html', {'form': form})

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