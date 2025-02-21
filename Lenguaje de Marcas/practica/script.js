// Crea una página web con un tipo de objeto (clase) definido por ti que contenga:

// 3 propiedades

// 1 método que admita 2 parámetros y que modifique las propiedades pero que no devuelva nada

// 1 método que no admita parámetros pero que devuelva el contenido de todas las propiedades


// Crear clase
let estado = false;

class Mango {
    constructor(nombre, maduro, color) {
        this.nombre = nombre;
        this.maduro = maduro;
        this.color = color;
    }

    cambio() {
        if (estado = false){
            let estado = true;
        } else {
            let estado = false
        }
    }

    listarMango() {
        if (this.maduro === true) {
            if (estado == false) {
                return `Nombre del mango: ${this.nombre}, ¿Está maduro?: Sí, Color: ${this.color}`;
            } else {
                return `Nombre del mango: ${this.nombre}, ¿Está maduro?: Sí, Color: ${this.color}, Placeholder: que?`;
            }
        } else {
            if (estado == false) {
                return `Nombre del mango: ${this.nombre}, ¿Está maduro?: No, Color: ${this.color}`;
            } else {
                return `Nombre del mango: ${this.nombre}, ¿Está maduro?: No, Color: ${this.color}, Placeholder: que?`;
            }
        }
    }
}

// Definir objetos
let objetoA = new Mango('Carlos', true, 'Verde');
let objetoB = new Mango('Simón José Antonio de la Santísima Trinidad Bolívar Palacios Ponte y Blanco', false, 'Rojo');

// Función para mostrar los mangos
function mostrarInfo() {
    document.getElementById('objA').innerText = objetoA.listarMango();
    document.getElementById('objB').innerText = objetoB.listarMango();
}

window.onload = mostrarInfo;
