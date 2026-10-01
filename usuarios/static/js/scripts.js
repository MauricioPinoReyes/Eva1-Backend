// ============================================
// Validar coincidencia de contraseñas (registro)
// ============================================
const pass1 = document.getElementById('pass1');
const pass2 = document.getElementById('pass2');
const msgCoincidencia = document.getElementById('coincidencia');

if (pass1 && pass2 && msgCoincidencia) {
    pass2.addEventListener('input', function () {
        if (pass1.value !== pass2.value) {
            msgCoincidencia.textContent = "Las contraseñas no coinciden";
            msgCoincidencia.style.color = "red";
        } else {
            msgCoincidencia.textContent = "Las contraseñas coinciden ✓";
            msgCoincidencia.style.color = "green";
        }
    });
}


// ============================================
// Mostrar / ocultar contraseña (login)
// ============================================
/* const btnMostrar = document.getElementById('btnMostrar');
const passLogin = document.getElementById('passLogin');

if (btnMostrar && passLogin) {
    btnMostrar.addEventListener('click', function () {
        if (passLogin.type === "password") {
            passLogin.type = "text";
            this.textContent = "🙈";
        } else {
            passLogin.type = "password";
            this.textContent = "👁️";
        }
    });
} */