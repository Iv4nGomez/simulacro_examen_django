from django.db import models
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Proyecto(models.Model):

    class tipo_servicio_choices(models.TextChoices):
        CONSULTORIA = 'CO', 'Consultoria'
        DESARROLLO = 'DE', 'Desarrollo'
        DISENIO = 'DI', 'Diseño'
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen_destacada = models.ImageField(upload_to='imagenes_proyectos/')
    tipo_servicio = models.CharField(choices=tipo_servicio_choices.choices)
    fecha_fin = models.DateField()
    categorias = models.ManyToManyField(Categoria)
    
    def __str__(self):
        return f"{self.titulo}"

    def clean(self):
        if self.titulo in 'borrador':
            raise ValidationError('El titulo no puede contener la palabra borrador')
        return super().clean()
        
class Testimonio(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()

    def __str__(self):
        return f"{self.contenido} ({self.autor})"