from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Proyecto
from .forms import ProyectoForm
from django.urls import reverse_lazy

class verProyectos(ListView):
    model = Proyecto
    context_object_name = 'proyectos'
    template_name = 'core/ver_proyectos.html'

class crearProyecto(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/crear_proyecto.html'
    success_url = reverse_lazy('ver_proyectos')

def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'core/detalle_proyecto.html', {'proyecto':proyecto})

