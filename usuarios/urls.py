from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),              # raíz → login
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
]