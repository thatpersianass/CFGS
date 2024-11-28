# Proyecto de Gestión de Inventarios - Desarrollo de Aplicaciones Multiplataforma, Primer Año

## Descripción del Proyecto

Este proyecto es una aplicación de gestión de inventarios, diseñada para administrar productos dentro de una tienda o empresa. La aplicación permite realizar operaciones como agregar, modificar y eliminar productos del inventario, todo a través de una interfaz de línea de comandos (CLI). Está desarrollado como parte de un ciclo formativo de grado superior en **Desarrollo de aplicaciones multiplataforma**, específicamente del **primer año**.

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
5. [Licencia](#licencia)
6. [Aviso de Derechos de Autor](#aviso-de-derechos-de-autor)

---

## Objetivos del Proyecto

El objetivo principal de este proyecto es diseñar y desarrollar una aplicación que permita la gestión de inventarios de productos dentro de una tienda o empresa. Los productos deben poder ser organizados por categorías, y la aplicación debe ser capaz de manejar datos como códigos, descripciones, precios y cantidades de productos.

Además, la aplicación deberá ofrecer una interfaz sencilla en la que el usuario pueda interactuar fácilmente con el sistema, permitiendo realizar las acciones de administración necesarias, como agregar o modificar productos, asegurando siempre la validez de los datos introducidos.

---

## Tecnologías Utilizadas

- **Lenguaje de programación**: Python
- **IDE utilizado**: Visual Studio Code
- **Versiones**: 
  - Python 3.x
  - Sistema operativo: Compatible con Windows, Linux y macOS

---

## Instalación

Para instalar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:

   Si tienes acceso a este repositorio privado, clónalo usando el siguiente comando:

   ```bash
   git clone https://github.com/thatpersianass/CFGS.git
Instala las dependencias:

Si el proyecto requiere librerías externas, instálalas utilizando pip (aunque en este caso, este proyecto no tiene dependencias externas específicas):

bash
Copiar código
pip install -r requirements.txt
Ejecuta el programa:

Para ejecutar el programa, solo necesitas iniciar el script principal del proyecto en tu terminal:

bash
Copiar código
python main.py
Estructura del Proyecto
La estructura de carpetas del proyecto es la siguiente:

bash
Copiar código
CFGS/
│
├── main.py               # Archivo principal que ejecuta el programa
├── productos.py          # Contiene las estructuras de datos para los productos
├── empresa.py            # Información sobre los productos de diferentes empresas
├── README.md             # Documentación del proyecto
└── LICENSE               # Archivo de licencia
Licencia
Este proyecto está bajo la Licencia MIT, lo que permite su uso, modificación y distribución bajo ciertas condiciones. Sin embargo, dado que este repositorio es privado, no se aceptan contribuciones externas.

Aviso de Derechos de Autor
Copyright (c) 2024 Persii - Marcos J.

Este software es de propiedad del autor y no está permitido su uso fuera del contexto educativo del ciclo formativo de "Desarrollo de aplicaciones multiplataforma, primer año". No se permite la distribución ni la modificación sin el permiso explícito del autor.
