
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),  # Página principal (lista de artículos)
    path('articulo/<int:id>/', views.detalle_articulo, name='detalle_articulo'),  # Detalle de un artículo
    # Otras rutas para crear, editar y eliminar artículos y comentarios
]
