from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('', views.login_view), # La raíz lleva al login
]