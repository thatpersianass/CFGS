-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS LogisticaTransportes;
USE LogisticaTransportes;

-- Tabla de Clientes
CREATE TABLE Clientes (
    DNI_cliente VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20)
);

-- Tabla de Conductores
CREATE TABLE Conductores (
    DNI_conductor VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    licencia_conduccion VARCHAR(50) NOT NULL,
    fecha_vencimiento_licencia DATE,
    telefono VARCHAR(20)
);

-- Tabla de Vehículos
CREATE TABLE Vehiculos (
    placa VARCHAR(20) PRIMARY KEY,
    tipo_vehiculo VARCHAR(50),
    capacidad DECIMAL(10,2), -- en toneladas
    estado ENUM('Disponible', 'En Ruta', 'En Mantenimiento') DEFAULT 'Disponible'
);

-- Tabla de Rutas
CREATE TABLE Rutas (
    id_ruta INT AUTO_INCREMENT PRIMARY KEY,
    origen VARCHAR(100) NOT NULL,
    destino VARCHAR(100) NOT NULL,
    distancia_km DECIMAL(10,2),
    tiempo_estimado_horas DECIMAL(5,2)
);

-- Tabla de Envíos
CREATE TABLE Envios (
    id_envio INT AUTO_INCREMENT PRIMARY KEY,
    DNI_cliente VARCHAR(20),
    DNI_conductor VARCHAR(20),
    placa VARCHAR(20),
    id_ruta INT,
    fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado_envio ENUM('Pendiente', 'En tránsito', 'Entregado', 'Cancelado') DEFAULT 'Pendiente',
    FOREIGN KEY (DNI_cliente) REFERENCES Clientes(DNI_cliente),
    FOREIGN KEY (DNI_conductor) REFERENCES Conductores(DNI_conductor),
    FOREIGN KEY (placa) REFERENCES Vehiculos(placa),
    FOREIGN KEY (id_ruta) REFERENCES Rutas(id_ruta)
);

