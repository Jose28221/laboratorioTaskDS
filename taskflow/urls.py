from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views # Importamos el Auth de Django
from tareas import views as tareas_views # Importamos nuestras vistas de tareas

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de Autenticación
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', tareas_views.dashboard, name='dashboard'),
    path('nueva-tarea/', tareas_views.crear_tarea, name='crear_tarea'),
    path('crear-proyecto/', tareas_views.crear_proyecto, name='crear_proyecto'),

]
