# Desarrollo de Aplicaciones Multiplataforma - CFGS

## Descripción del Proyecto

Este proyecto es una aplicación de gestión de inventarios, diseñada para administrar productos dentro de una tienda o empresa. La aplicación permite realizar operaciones como agregar, modificar y eliminar productos del inventario, todo a través de una interfaz de línea de comandos (CLI). Está desarrollado como parte de un ciclo formativo de grado superior en desarrollo de aplicaciones multiplataforma (CFGS).

Los productos se pueden categorizar en varias categorías como "frío", "verduras", "lácteos", etc. Cada producto tiene un código único generado de forma automática que permite su identificación en el inventario. Además, la aplicación ofrece la posibilidad de gestionar inventarios de productos proporcionados por diferentes empresas externas.

### Funcionalidades principales:

- **Gestión de productos**: Agregar, eliminar y modificar productos en el inventario.
- **Códigos únicos de productos**: Los productos tienen un código único basado en su categoría y un número de 4 dígitos.
- **Gestión de cantidades y precios**: Actualización de cantidades de productos y modificación de precios.
- **Interfaz de línea de comandos (CLI)**: La interacción con el sistema se realiza a través de la terminal de comandos.
- **Validación de datos**: Verificación de códigos de productos únicos, precios en formato decimal y cantidades como números enteros.

---

## Índice

1. [Objetivos del Proyecto](#objetivos-del-proyecto)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
3. [Instalación](#instalación)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Reglas y Normas del Proyecto](#reglas-y-normas-del-proyecto)
6. [Flujo de Trabajo](#flujo-de-trabajo)
7. [Uso de la Aplicación](#uso-de-la-aplicación)
8. [Contribuciones](#contribuciones)
9. [Licencia](#licencia)
10. [Aviso de Derechos de Autor](#aviso-de-derechos-de-autor)

---

## Objetivos del Proyecto

El objetivo principal del proyecto es desarrollar una herramienta eficaz para la gestión de inventarios, con funcionalidades que permitan a los usuarios añadir productos, modificarlos y gestionar el inventario de manera eficiente. Este sistema de gestión de inventarios también está diseñado para ser fácil de usar, con un enfoque en la simplicidad y la efectividad.

### Objetivos específicos:
- **Generación de códigos de productos únicos**: El código de cada producto se genera automáticamente, combinando la primera letra de la categoría del producto y un número secuencial.
- **Modificación de productos**: Si un código ya existe, se permite modificar la cantidad o el precio sin tener que ingresar de nuevo la descripción del producto.
- **Interacción sencilla**: A través de la interfaz de línea de comandos (CLI), el sistema interactúa de forma sencilla con el usuario para gestionar el inventario.

---

## Tecnologías Utilizadas

Este proyecto se ha desarrollado utilizando las siguientes tecnologías:

- **Python 3.x**: Lenguaje de programación principal utilizado para implementar la lógica de la aplicación.
- **Git**: Sistema de control de versiones utilizado para gestionar el código fuente y colaborar en el proyecto.
- **GitHub**: Plataforma de alojamiento de código y colaboración remota.
- **Visual Studio Code (VSCode)**: Editor de código utilizado para escribir y desarrollar el proyecto.
- **Terminal/Consola de Comandos**: La interacción con el sistema se realiza a través de la terminal.

---

## Instalación

Para instalar y ejecutar este proyecto en tu máquina local, sigue los siguientes pasos:

### Requisitos previos
- **Python 3.x**: Verifica si Python está instalado ejecutando `python --version` o `python3 --version` en la terminal. Si no está instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- **Git**: Si no tienes Git instalado, puedes obtenerlo desde [git-scm.com](https://git-scm.com/).

### Pasos de Instalación

1. **Clonar el repositorio**: Para obtener el código fuente en tu máquina local, ejecuta el siguiente comando en tu terminal:

   ```bash
   git clone https://github.com/thatpersianass/CFGS.git

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

Derechos de autor (c) 2024, Persii - Marcos J. Todos los derechos reservados.
