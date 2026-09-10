from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  
from .models import Usuario
import re

# --- VISTA DE REGISTRO ---
def registro(request):
    mensaje_error = ""
    if request.method == "POST":
        nombre = request.POST.get('nombre') 
        correo = request.POST.get('correo')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Validaciones
        if Usuario.objects.filter(nombre_usuario=nombre).exists():
            mensaje_error = "El nombre de usuario ya existe."
        elif Usuario.objects.filter(correo=correo).exists():
            mensaje_error = "El correo electrónico ya está registrado."
        elif pass1 != pass2:
            mensaje_error = "Las contraseñas no coinciden."
        elif len(pass1) < 8 or not re.search(r"[A-Z]", pass1) or not re.search(r"[0-9]", pass1):
            mensaje_error = "La contraseña debe tener 8 caracteres, una mayúscula y un número."
        else:
            # Guardar en BD
            Usuario.objects.create(nombre_usuario=nombre, correo=correo, contrasena=pass1)
            messages.success(request, "Se ha registrado correctamente.") 
            return redirect('login') # Redirigir al login

    return render(request, 'registro.html', {'error': mensaje_error})

# --- VISTA DE LOGIN ---
def login_view(request):
    mensaje_error = ""
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        pass_ingresada = request.POST.get('pass')

        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre)
            
            if usuario.bloqueado:
                mensaje_error = "Clave bloqueada. Ha superado el máximo de intentos permitidos."
            elif usuario.contrasena == pass_ingresada:
                usuario.intentos_fallidos = 0
                usuario.save()
                return render(request, 'bienvenida.html', {'usuario': usuario.nombre_usuario})
            else:
                usuario.intentos_fallidos += 1
                if usuario.intentos_fallidos >= 3:
                    usuario.bloqueado = True
                    mensaje_error = "Clave bloqueada. Ha superado el máximo de intentos permitidos."
                else:
                    mensaje_error = f"Contraseña incorrecta. Intentos restantes: {3 - usuario.intentos_fallidos}"
                usuario.save()
        except Usuario.DoesNotExist:
            mensaje_error = "El usuario no existe."

    return render(request, 'login.html', {'error': mensaje_error})

# --- VISTA DE BIENVENIDA ---
def bienvenida(request):
    return render(request, 'bienvenida.html')