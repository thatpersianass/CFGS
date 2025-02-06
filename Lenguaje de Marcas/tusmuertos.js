function validarFormulario(event) {
    let email = document.getElementById("email").value;
    let telefono = document.getElementById("telefono").value;
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    let telefonoRegex = /^\d{9,15}$/; // Acepta entre 9 y 15 dígitos
    
    if (!telefonoRegex.test(telefono)) {
        alert("Por favor, ingrese un número de teléfono válido (9-15 dígitos).");
        return;
    }
    
    if (email !== "" && !emailRegex.test(email)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return;
    }
    
    document.getElementById("formulario").submit();
}