from django.shortcuts import render, redirect

from . import models, forms


def index(request):
    return render(request, "producto/index.html")


def productocategoria_list(request):
    productocategoria = models.ProductoCategoria.objects.all()
    contexto = {"productocategoria": productocategoria}
    return render(request, "producto/productocategoria_list.html", contexto)


def productocategoria_create(request):
    if request.method == "GET":
        form = forms.ProductoCategoriaForm()
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:productocategoria_list")

    contexto = {"form": form}
    return render(request, "producto/productocategoria_create.html", contexto)
