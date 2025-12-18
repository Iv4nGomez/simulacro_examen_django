from django.forms import ModelForm
from .models import Proyecto, Testimonio
from datetime import date
from django.core.exceptions import ValidationError

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'imagen_destacada','fecha_fin', 'categorias', 'tipo_servicio']

    def clean_fecha_fin(self):

        fecha_fin = self.cleaned_data['fecha_fin']
        if fecha_fin > date(2026, 12, 17):
            raise ValidationError('Esta fecha es muy lejana tienes que poner la fecha que no supere el año')
        return fecha_fin
    
class TestimonioForm(ModelForm):
    class Meta:
        model = Testimonio
        fields = ['proyecto', 'autor', 'contenido']