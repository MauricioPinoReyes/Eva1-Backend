from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
import re

Usuario = get_user_model()


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-text'})
        self.fields['email'].widget.attrs.update({'class': 'input-text'})
        self.fields['password1'].widget.attrs.update({'class': 'input-text', 'id': 'pass1'})
        self.fields['password2'].widget.attrs.update({'class': 'input-text', 'id': 'pass2'})

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1', '')
        if len(password) < 8:
            raise forms.ValidationError("Debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", password):
            raise forms.ValidationError("Debe contener al menos una mayúscula.")
        if not re.search(r"[0-9]", password):
            raise forms.ValidationError("Debe contener al menos un número.")
        return password