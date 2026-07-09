from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # Importamos el Auth de Django
from tareas import views as tareas_views  # Importamos nuestras vistas de tareas

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de autenticación (login / logout)
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Ruta principal: dashboard (requiere login)
    path('', tareas_views.dashboard, name='dashboard'),

    # Rutas de gestión
    path('proyectos/nuevo/', tareas_views.crear_proyecto, name='crear_proyecto'),
    path('tareas/nueva/', tareas_views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/completar/', tareas_views.completar_tarea, name='completar_tarea'),
]
