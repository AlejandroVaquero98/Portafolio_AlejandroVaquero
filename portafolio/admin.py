from django.contrib import admin
from .models import Project

# Para añadir el modelo de los projectos al panel admin
admin.site.register(Project)
