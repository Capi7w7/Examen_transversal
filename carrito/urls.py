from django.urls import path
from . import views

urlpatterns = [
    path('agregar/<int:repuesto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:repuesto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
]
