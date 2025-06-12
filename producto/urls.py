from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.index, name="index"),
    # URLs para ProductoCategoria
    path(
        "productocategoria/list/",
        views.ProductoCategoriaListView.as_view(),
        name="productocategoria_list",
    ),
    path(
        "productocategoria/create/",
        views.ProductoCategoriaCreateView.as_view(),
        name="productocategoria_create",
    ),
    path(
        "productocategoria/update/<int:pk>",
        views.ProductoCategoriaUpdateView.as_view(),
        name="productocategoria_update",
    ),
    path(
        "productocategoria/detail/<int:pk>",
        views.ProductoCategoriaDetailView.as_view(),
        name="productocategoria_detail",
    ),
    path(
        "productocategoria/delete/<int:pk>",
        views.ProductoCategoriaDeleteView.as_view(),
        name="productocategoria_delete",
    ),
    # URLs para Producto
    path(
        "producto/list/",
        views.ProductoListView.as_view(),
        name="producto_list",
    ),
    path(
        "producto/create/",
        views.ProductoCreateView.as_view(),
        name="producto_create",
    ),
    path(
        "producto/update/<int:pk>",
        views.ProductoUpdateView.as_view(),
        name="producto_update",
    ),
    path(
        "producto/detail/<int:pk>",
        views.ProductoDetailView.as_view(),
        name="producto_detail",
    ),
    path(
        "producto/delete/<int:pk>",
        views.ProductoDeleteView.as_view(),
        name="producto_delete",
    ),
]
