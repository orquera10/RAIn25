from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from . import models, forms


def index(request):
    return render(request, "producto/index.html")


class ProductoCategoriaListView(ListView):
    model = models.ProductoCategoria

    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            queryset = models.ProductoCategoria.objects.all()
        return queryset


class ProductoCategoriaCreateView(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaUpdateView(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaDetailView(DetailView):
    model = models.ProductoCategoria


class ProductoCategoriaDeleteView(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")


# Vistas para el modelo Producto
class ProductoListView(ListView):
    model = models.Producto
    context_object_name = "productos"

    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            queryset = models.Producto.objects.all()
        return queryset


class ProductoCreateView(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoUpdateView(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDetailView(DetailView):
    model = models.Producto


class ProductoDeleteView(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")