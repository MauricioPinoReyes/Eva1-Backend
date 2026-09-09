// Validar coincidencia de contraseñas en el registro
let pass1 = document.getElementById('pass1');
let pass2 = document.getElementById('pass2');
let msgCoincidencia = document.getElementById('coincidencia');

if(pass2) {
    pass2.addEventListener('input', function() {
        if (pass1.value !== pass2.value) {
            msgCoincidencia.textContent = "Las contraseñas no coinciden";
        } else {
            msgCoincidencia.textContent = "Las contraseñas coinciden. ";
            msgCoincidencia.style.color = "green";
        }
    });
}

// Mostrar/Ocultar contraseña en el login
let btnMostrar = document.getElementById('btnMostrar');
let passLogin = document.getElementById('passLogin');

if(btnMostrar) {
    btnMostrar.addEventListener('click', function() {
        if (passLogin.type === "password") {
            passLogin.type = "text";
        } else {
            passLogin.type = "password";
        }
    });
}