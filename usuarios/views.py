from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

Usuario = get_user_model()

MAX_INTENTOS = 3


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha registrado correctamente.")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        pass_ingresada = request.POST.get('pass')

        # Verificar bloqueo
        try:
            usuario_obj = Usuario.objects.get(username=nombre)
            if usuario_obj.bloqueado:
                messages.error(request, "Clave bloqueada. Contacta al administrador.")
                return render(request, 'login.html')
        except Usuario.DoesNotExist:
            usuario_obj = None

        # Autenticar
        user = authenticate(request, username=nombre, password=pass_ingresada)

        if user is not None:
            user.intentos_fallidos = 0
            user.save()
            login(request, user)
            return redirect('bienvenida')
        else:
            if usuario_obj:
                usuario_obj.intentos_fallidos += 1
                restantes = MAX_INTENTOS - usuario_obj.intentos_fallidos
                if usuario_obj.intentos_fallidos >= MAX_INTENTOS:
                    usuario_obj.bloqueado = True
                    messages.error(request, "Clave bloqueada. Ha superado el máximo de intentos.")
                else:
                    messages.error(request, f"Contraseña incorrecta. Intentos restantes: {restantes}")
                usuario_obj.save()
            else:
                messages.error(request, "El usuario no existe.")

    return render(request, 'login.html')


@login_required
def bienvenida(request):
    return render(request, 'bienvenida.html', {'usuario': request.user.username})


def logout_view(request):
    logout(request)
    return redirect('login')