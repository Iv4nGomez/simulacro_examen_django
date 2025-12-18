
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', verProyectos.as_view(), name='ver_proyectos'),
    path('crear_proyecto/', crearProyecto.as_view(), name='crear_proyecto'),
    path('detalle_proyecto/<int:pk>', detalle_proyecto, name='detalle_proyecto'),
    path('crear_testimonio', crear_testimonio, name='crear_testimonio')
]


