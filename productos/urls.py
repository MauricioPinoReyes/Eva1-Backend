from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.mostrarIndex, name='index'),
    path('form_registrar', views.mostrarFormRegistrar, name='form_registrar'),
    path('listado', views.mostrarListado, name='listado'),
    path('form_actualizar/<int:id>', views.mostrarFormActualizar, name='form_actualizar'),
    path('insertar', views.insertarProducto, name='insertar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
]