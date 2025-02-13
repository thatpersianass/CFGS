let encendida = false;
let stream = null;
let track = null;

async function toggleBombisha() {
    let bombisha = document.getElementById('bombisha');
    let boton = document.getElementById('toggle');

    if (encendida) {
        bombisha.src = "pic_bulboff.gif"; // Apagar bombilla
        boton.textContent = "Encender"; // Cambiar texto del botón
        apagarLinterna();
    } else {
        bombisha.src = "pic_bulbon.gif"; // Encender bombilla
        boton.textContent = "Apagar"; // Cambiar texto del botón
        encenderLinterna();
    }

    encendida = !encendida; // Alternar estado
}

async function encenderLinterna() {
    try {
        if (!stream) {
            stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
            track = stream.getVideoTracks()[0];
        }
        if (track) {
            await track.applyConstraints({ advanced: [{ torch: true }] }); // Enciende el flash
        }
    } catch (error) {
        console.error("No se pudo acceder a la linterna:", error);
    }
}

function apagarLinterna() {
    if (track) {
        track.stop(); // Apaga la linterna
        track = null;
        stream = null;
    }
}
