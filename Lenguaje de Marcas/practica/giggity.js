<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clase Coche</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        input, button {
            margin: 10px;
            padding: 10px;
        }
    </style>
</head>
<body>

    <h1>Información del Coche</h1>
    <p id="info"></p>

    <label for="modelo">Nuevo Modelo:</label>
    <input type="text" id="modelo">

    <label for="velocidad">Nueva Velocidad:</label>
    <input type="number" id="velocidad">

    <button onclick="actualizarCoche()">Actualizar Coche</button>

    <script>
        class Coche {
            constructor(marca, modelo, velocidad) {
                this.marca = marca;
                this.modelo = modelo;
                this.velocidad = velocidad;
            }

            actualizarDatos(nuevoModelo, nuevaVelocidad) {
                this.modelo = nuevoModelo;
                this.velocidad = nuevaVelocidad;
            }

            obtenerDatos() {
                return `Marca: ${this.marca}, Modelo: ${this.modelo}, Velocidad: ${this.velocidad} km/h`;
            }
        }

        // Crear una instancia de Coche
        let miCoche = new Coche("Toyota", "Corolla", 120);

        function mostrarInfo() {
            document.getElementById("info").innerText = miCoche.obtenerDatos();
        }

        function actualizarCoche() {
            let nuevoModelo = document.getElementById("modelo").value;
            let nuevaVelocidad = document.getElementById("velocidad").value;

            if (nuevoModelo && nuevaVelocidad) {
                miCoche.actualizarDatos(nuevoModelo, parseInt(nuevaVelocidad));
                mostrarInfo();
            } else {
                alert("Por favor, ingrese todos los valores.");
            }
        }

        // Mostrar la información inicial
        mostrarInfo();
    </script>

</body>
</html>
