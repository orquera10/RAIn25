from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from . import models, forms


def index(request):
    return render(request, "producto/index.html")


# def productocategoria_list(request):
#     productocategoria = models.ProductoCategoria.objects.all()
#     contexto = {"productocategoria": productocategoria}
#     return render(request, "producto/productocategoria_list.html", contexto)

class ProductoCategoriaListView(ListView):
    model = models.ProductoCategoria
    # context_object_name = "productocategoria"
    # template_name = "producto/productocategoria_list.html"

    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            queryset = models.ProductoCategoria.objects.all()
        return queryset



# def productocategoria_create(request):
#     if request.method == "GET":
#         form = forms.ProductoCategoriaForm()
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:productocategoria_list")

#     contexto = {"form": form}
#     return render(request, "producto/productocategoria_create.html", contexto)

class ProductoCategoriaCreateView(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    # template_name = "producto/productocategoria_create.html"

class ProductoCategoriaUpdateView(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaDetailView(DetailView):
    model = models.ProductoCategoria


class ProductoCategoriaDeleteView(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")