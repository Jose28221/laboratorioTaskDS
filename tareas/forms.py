from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'proyecto', 'asignada_a']
        # No agregamos 'completada' porque por defecto será False al crear una nueva tarea. 