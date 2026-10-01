from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'intentos_fallidos', 'bloqueado', 'is_staff')
    list_filter = ('bloqueado', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Control de acceso', {'fields': ('intentos_fallidos', 'bloqueado')}),
    )