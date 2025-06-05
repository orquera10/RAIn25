from django.shortcuts import render

from . import models


def index(request):
    return render(request, "producto/index.html")


def productocategoria_list(request):
    productocategoria = models.ProductoCategoria.objects.all()
    contexto = {"productocategoria": productocategoria}
    return render(request, "producto/productocategoria_list.html", contexto)
