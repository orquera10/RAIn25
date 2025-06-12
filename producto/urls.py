from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.index, name="index"),
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
]
