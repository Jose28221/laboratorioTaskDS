from django.contrib import admin
from .models import Proyecto, Tarea
# Register your models here.
# Le decimos a Django que muestre esta tabla en el panel
admin.site.register(Proyecto)
admin.site.register(Tarea)