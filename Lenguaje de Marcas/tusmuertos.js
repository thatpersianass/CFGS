// function mostrarPoia() {
//     document.getElementById('texto').innerHTML = 'Adios mundo cruel';
// }

let coches = ['seat', 'bmw', 'ford', 'byd'];
let contador = 0;

document.getElementById('texto').innerHTML = (coches[contador]);

function mostrarPoia() {
    contador++; // Aumentar el contador

    if (contador >= coches.length) {
        contador = 0; // Reiniciar el contador si se excede
    }

    document.getElementById('texto').innerHTML = coches[contador];
}