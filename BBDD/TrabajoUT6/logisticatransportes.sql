CREATE DATABASE  IF NOT EXISTS `logisticatransportes` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `logisticatransportes`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: logisticatransportes
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `DNI_cliente` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`DNI_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES ('10229187','Azahar Valera Vilar','Alameda Tecla Riba 56 Puerta 8 , Zamora, 24307','+34 894199197'),('10870440','Eloy Heras Sancho','Paseo de Tristán Aroca 30, Lleida, 13276','+34 635 137 889'),('11220300','Poncio Arjona-Gil','Acceso de Pablo Pou 94, Murcia, 72471','+34731 10 63 70'),('12165831','Pancho Cuevas-Bartolomé','Camino de Xavier Fabra 36 Puerta 4 , Tarragona, 42284','+34 621047980'),('13049466','Adriana Ricart Ropero','C. Jacobo Rico 194, Pontevedra, 49047','+34641 048 914'),('13429114','Chucho Álvarez','Plaza Rosendo Casares 92 Apt. 37 , Badajoz, 65814','+34 711608606'),('14173992','Martin Torrijos Pineda','Rambla de Benita Marco 42, Álava, 82987','+34736 72 00 16'),('14962756','Anselmo Arregui Priego','Avenida Filomena Llano 2, Las Palmas, 99938','+34 739 710 372'),('16323012','Lucía Sevilla','Callejón de Chuy Jaume 73, Álava, 83385','+34747 20 61 90'),('21810468','Evelia Sancho Torrecilla','Via José Cruz 3, León, 92869','+34 727344869'),('22042015','Mercedes Román Medina','Pasaje de Manu Gallardo 52 Puerta 1 , León, 05128','+34705097693'),('28295147','Ainara Mamen Ricart Gelabert','Camino de Ovidio Sureda 81 Apt. 71 , Ávila, 26210','+34715 13 52 88'),('2854398','Gaspar del Mulet','C. Luisina Torre 82 Apt. 87 , Badajoz, 09766','+34748 951 330'),('34841517','Juanita Verónica Salamanca Laguna','Alameda Ruperto Parejo 8 Apt. 56 , Valladolid, 50083','+34 742748355'),('34910462','María Luisa Pacheco Salamanca','Glorieta de Hermenegildo Hernández 4 Puerta 7 , Ourense, 15885','+34 925 649 615'),('41402669','Yaiza Higueras Botella','Rambla de Emilio Segovia 3, Tarragona, 20165','+34744 713 114'),('48155019','Trini Meléndez-Jordá','Vial María Ángeles Guillen 84, Lugo, 42829','+34 978433967'),('51272891','Adolfo Ramírez-Ferrando','Rambla Carlos Guerrero 33, Córdoba, 35722','+34 704 02 48 45'),('58898480','María Cervera Mata','Pasaje de Wilfredo Elorza 62, Zamora, 23617','+34741 475 106'),('61052190','Florina Hilda Cortina Higueras','Glorieta de Leticia Alemany 77, Baleares, 98944','+34 805968039'),('61302101','Constanza Chelo Noriega Gonzalez','Callejón Jose Francisco Seguí 62, Santa Cruz de Tenerife, 82571','+34 701 162 795'),('68130219','Candelario Jurado Malo','Rambla Lisandro Jerez 51, León, 14190','+34 647 37 52 64'),('68397519','Anselma Roldán-Roldán','Glorieta Rafaela Pinedo 54, Segovia, 14825','+34924 94 07 88'),('76350246','Sabina Guijarro Gomis','Paseo Concepción Tomás 49 Piso 1 , Murcia, 22366','+34 703213583'),('81408418','Amaro Rozas Batlle','Paseo Guillermo Ayala 13 Puerta 5 , Huelva, 00581','+34 870 690 524'),('83695977','Dalila Rincón Cobos','Alameda Jenny Pagès 180 Piso 9 , Toledo, 02017','+34727 92 16 85'),('90311040','Íngrid Franco Arnaiz','Ronda de Corona Martin 605, Pontevedra, 15362','+34829 68 10 59'),('92986727','Juan Pablo Roldan Boix','Vial Buenaventura Arteaga 55, Las Palmas, 32487','+34 635 015 703'),('93503963','Edgardo Criado Conesa','Paseo Rufina Esparza 88, Zamora, 39810','+34 677089415'),('95892193','Emilia del Castilla','Ronda de Nuria Montesinos 8 Piso 8 , Castellón, 71378','+34 830 85 09 60');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conductores`
--

DROP TABLE IF EXISTS `conductores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conductores` (
  `DNI_conductor` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `licencia_conduccion` varchar(50) NOT NULL,
  `fecha_vencimiento_licencia` date DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`DNI_conductor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conductores`
--

LOCK TABLES `conductores` WRITE;
/*!40000 ALTER TABLE `conductores` DISABLE KEYS */;
INSERT INTO `conductores` VALUES ('1529504','Héctor del Miró','imh-3234','2029-07-28','+34 862 64 31 50'),('24560724','Blanca Ferrando-Luque','dQk-8317','2028-10-27','+34 808300837'),('28464231','Florentino Benitez Cerdán','cSB-9579','2029-09-10','+34 646595034'),('29177597','Porfirio Armas Prada','ZEJ-2103','2030-03-05','+34721 533 013'),('33278861','Zaida Montaña Avilés','MlY-2915','2028-03-27','+34 743 318 006'),('3766878','Eva María Múgica','JOh-6010','2028-12-09','+34 746671471'),('4284617','Juan José Bárcena Barco','Xve-8615','2026-05-22','+34 721 07 68 39'),('50332090','Catalina Pérez Martí','ufL-9994','2027-02-05','+34 866 233 774'),('55639481','Emiliana Porras Benet','oBp-3087','2026-12-19','+34740863394'),('57674055','Juan Manuel Mena Vilanova','GdC-6558','2026-09-05','+34 746 606 944'),('75625648','Isaac Ferrándiz Montero','uHJ-1539','2029-01-17','+34 731753253'),('75967676','Anita de Batlle','EHy-2609','2028-04-24','+34721 960 887'),('80152664','Felipa del Casado','Kmk-7878','2029-01-18','+34 718 81 51 16'),('80433832','Francisca Alvarez Mateos','Yff-2655','2029-05-24','+34 719558226'),('97647642','Adora Iglesia Heredia','XyT-2885','2027-12-20','+34948370392');
/*!40000 ALTER TABLE `conductores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `envios`
--

DROP TABLE IF EXISTS `envios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `envios` (
  `id_envio` int NOT NULL AUTO_INCREMENT,
  `DNI_cliente` varchar(20) DEFAULT NULL,
  `DNI_conductor` varchar(20) DEFAULT NULL,
  `placa` varchar(20) DEFAULT NULL,
  `id_ruta` int DEFAULT NULL,
  `fecha_envio` datetime DEFAULT CURRENT_TIMESTAMP,
  `estado_envio` enum('Pendiente','En tránsito','Entregado','Cancelado') DEFAULT 'Pendiente',
  PRIMARY KEY (`id_envio`),
  KEY `DNI_cliente` (`DNI_cliente`),
  KEY `DNI_conductor` (`DNI_conductor`),
  KEY `placa` (`placa`),
  KEY `id_ruta` (`id_ruta`),
  CONSTRAINT `envios_ibfk_1` FOREIGN KEY (`DNI_cliente`) REFERENCES `clientes` (`DNI_cliente`),
  CONSTRAINT `envios_ibfk_2` FOREIGN KEY (`DNI_conductor`) REFERENCES `conductores` (`DNI_conductor`),
  CONSTRAINT `envios_ibfk_3` FOREIGN KEY (`placa`) REFERENCES `vehiculos` (`placa`),
  CONSTRAINT `envios_ibfk_4` FOREIGN KEY (`id_ruta`) REFERENCES `rutas` (`id_ruta`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `envios`
--

LOCK TABLES `envios` WRITE;
/*!40000 ALTER TABLE `envios` DISABLE KEYS */;
INSERT INTO `envios` VALUES (1,'92986727','75625648','wzx-3684',13,'2025-04-21 15:58:14','En tránsito'),(2,'22042015','75625648','zGB-1710',7,'2025-01-14 06:22:00','Cancelado'),(3,'76350246','75967676','kAk-1400',7,'2025-01-16 20:12:32','Entregado'),(4,'61052190','80433832','Gha-9792',30,'2025-02-19 14:08:33','Cancelado'),(5,'51272891','33278861','Dvc-6795',19,'2025-03-21 14:26:42','Cancelado'),(6,'68397519','33278861','wuV-3597',3,'2025-01-06 01:26:59','Pendiente'),(7,'13429114','80433832','yYd-7922',29,'2025-04-17 15:16:38','Entregado'),(8,'28295147','75967676','DvZ-3164',22,'2025-04-15 22:06:41','Pendiente'),(9,'83695977','3766878','mIB-3960',19,'2025-01-02 21:04:58','Entregado'),(10,'81408418','80152664','vKw-3435',14,'2025-02-17 23:54:35','Cancelado'),(11,'2854398','28464231','wzs-0610',21,'2025-01-04 13:11:59','Entregado'),(12,'13049466','75967676','wzx-3684',11,'2025-01-01 04:35:23','Cancelado'),(13,'81408418','50332090','vKw-3435',24,'2025-04-12 05:45:51','Entregado'),(14,'76350246','75625648','Vea-6084',18,'2025-03-03 22:01:53','En tránsito'),(15,'76350246','28464231','zPQ-0582',22,'2025-01-28 00:22:53','Cancelado'),(16,'76350246','80433832','wzx-3684',1,'2025-01-09 18:58:20','En tránsito'),(17,'76350246','33278861','SKT-4640',18,'2025-02-03 13:23:22','En tránsito'),(18,'22042015','80152664','zGB-1710',24,'2025-01-07 18:56:24','Cancelado'),(19,'92986727','3766878','SKT-4640',1,'2025-03-20 20:22:46','Entregado'),(20,'34841517','55639481','Esj-9676',4,'2025-01-19 22:06:34','Pendiente'),(21,'2854398','3766878','Dvc-6795',1,'2025-03-22 18:54:11','Pendiente'),(22,'61302101','24560724','Dvc-6795',9,'2025-04-08 12:13:37','En tránsito'),(23,'13429114','97647642','yYd-7922',22,'2025-02-11 02:21:31','Pendiente'),(24,'13049466','80433832','luw-3286',30,'2025-02-04 08:21:28','Cancelado'),(25,'81408418','75625648','zaH-0048',3,'2025-03-03 01:31:58','Entregado'),(26,'12165831','24560724','wuV-3597',22,'2025-02-18 18:46:10','Pendiente'),(27,'61302101','29177597','yYd-7922',6,'2025-01-21 22:41:26','En tránsito'),(28,'22042015','24560724','vKw-3435',18,'2025-01-30 05:21:41','Pendiente'),(29,'34841517','33278861','mIB-3960',11,'2025-03-25 04:03:07','Cancelado'),(30,'34910462','50332090','vLP-5758',8,'2025-03-12 10:45:27','Entregado'),(31,'2854398','50332090','zaH-0048',19,'2025-02-22 09:39:20','Cancelado'),(32,'58898480','57674055','cdc-9029',16,'2025-03-12 03:54:48','En tránsito'),(33,'41402669','33278861','Vea-6084',23,'2025-01-02 10:15:35','Entregado'),(34,'14173992','4284617','cdc-9029',1,'2025-01-30 00:27:55','En tránsito'),(35,'16323012','1529504','mIB-3960',9,'2025-02-06 20:13:14','En tránsito'),(36,'21810468','57674055','luw-3286',30,'2025-03-20 05:38:31','Cancelado'),(37,'16323012','55639481','DvZ-3164',8,'2025-01-04 20:31:41','Pendiente'),(38,'13429114','28464231','zPQ-0582',6,'2025-01-18 17:18:02','En tránsito'),(39,'10229187','57674055','wzx-3684',30,'2025-04-04 01:42:03','Entregado'),(40,'83695977','97647642','Dvc-6795',17,'2025-04-03 17:36:35','Pendiente'),(41,'95892193','1529504','Esj-9676',16,'2025-04-05 11:50:48','Pendiente'),(42,'22042015','29177597','Gha-9792',5,'2025-03-11 15:06:30','Pendiente'),(43,'58898480','1529504','kAk-1400',10,'2025-04-13 01:47:29','Pendiente'),(44,'14173992','80433832','DvZ-3164',24,'2025-02-21 18:09:10','Entregado'),(45,'21810468','24560724','NmB-1303',21,'2025-01-31 22:59:01','En tránsito'),(46,'14962756','57674055','wzs-0610',25,'2025-01-27 05:24:30','En tránsito'),(47,'83695977','75967676','DvZ-3164',18,'2025-02-21 05:53:06','Pendiente'),(48,'93503963','55639481','Esj-9676',16,'2025-02-16 18:42:25','Entregado'),(49,'61052190','33278861','luw-3286',9,'2025-02-17 02:24:27','Entregado'),(50,'58898480','3766878','NmB-1303',26,'2025-01-29 09:55:21','Entregado');
/*!40000 ALTER TABLE `envios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rutas`
--

DROP TABLE IF EXISTS `rutas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rutas` (
  `id_ruta` int NOT NULL AUTO_INCREMENT,
  `origen` varchar(100) NOT NULL,
  `destino` varchar(100) NOT NULL,
  `distancia_km` decimal(10,2) DEFAULT NULL,
  `tiempo_estimado_horas` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id_ruta`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rutas`
--

LOCK TABLES `rutas` WRITE;
/*!40000 ALTER TABLE `rutas` DISABLE KEYS */;
INSERT INTO `rutas` VALUES (1,'Ciudad','Murcia',612.72,5.70),(2,'Pontevedra','Navarra',930.06,1.93),(3,'Cáceres','Huelva',313.30,7.27),(4,'Jaén','Valencia',772.17,11.70),(5,'La Rioja','Cuenca',435.92,23.46),(6,'Ávila','Guipúzcoa',721.00,13.09),(7,'Baleares','Guadalajara',295.95,21.22),(8,'Melilla','Pontevedra',904.02,18.95),(9,'Granada','Burgos',707.92,1.92),(10,'Albacete','Málaga',216.39,16.97),(11,'Ávila','Huelva',230.37,12.25),(12,'Toledo','Cáceres',969.52,9.26),(13,'Guadalajara','Valladolid',621.76,19.95),(14,'La Coruña','Ourense',785.54,20.99),(15,'Baleares','Pontevedra',89.19,4.71),(16,'Zamora','Lugo',250.33,21.73),(17,'Huesca','Lugo',202.70,20.06),(18,'Cáceres','Teruel',485.86,20.54),(19,'Vizcaya','Cáceres',340.15,4.02),(20,'Jaén','Valencia',336.90,17.77),(21,'Navarra','Jaén',288.49,3.34),(22,'Valladolid','Albacete',831.46,14.12),(23,'Tarragona','Madrid',126.32,13.92),(24,'Madrid','Tarragona',907.83,7.83),(25,'Zaragoza','Álava',449.12,19.61),(26,'Asturias','Toledo',197.67,18.35),(27,'Alicante','Cáceres',494.14,15.10),(28,'Ávila','Zamora',472.27,6.76),(29,'Castellón','Castellón',999.14,17.77),(30,'Alicante','Navarra',512.36,19.70);
/*!40000 ALTER TABLE `rutas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculos`
--

DROP TABLE IF EXISTS `vehiculos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehiculos` (
  `placa` varchar(20) NOT NULL,
  `tipo_vehiculo` varchar(50) DEFAULT NULL,
  `capacidad` decimal(10,2) DEFAULT NULL,
  `estado` enum('Disponible','En Ruta','En Mantenimiento') DEFAULT 'Disponible',
  PRIMARY KEY (`placa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculos`
--

LOCK TABLES `vehiculos` WRITE;
/*!40000 ALTER TABLE `vehiculos` DISABLE KEYS */;
INSERT INTO `vehiculos` VALUES ('cdc-9029','Furgoneta',12.08,'En Ruta'),('Dvc-6795','Furgoneta',16.71,'Disponible'),('DvZ-3164','Trailer',4.59,'En Ruta'),('Esj-9676','Furgoneta',5.56,'En Ruta'),('Gha-9792','Trailer',18.89,'Disponible'),('kAk-1400','Trailer',3.52,'Disponible'),('luw-3286','Camión',18.88,'En Ruta'),('mIB-3960','Camión',6.44,'En Ruta'),('NmB-1303','Trailer',18.59,'En Ruta'),('SKT-4640','Trailer',19.31,'En Mantenimiento'),('Vea-6084','Trailer',13.15,'En Ruta'),('vKw-3435','Camión',11.77,'En Mantenimiento'),('vLP-5758','Furgoneta',3.51,'Disponible'),('wuV-3597','Camión',16.26,'En Mantenimiento'),('wzs-0610','Camión',6.87,'En Ruta'),('wzx-3684','Furgoneta',19.60,'Disponible'),('yYd-7922','Trailer',15.58,'En Mantenimiento'),('zaH-0048','Camión',12.85,'En Ruta'),('zGB-1710','Furgoneta',2.89,'Disponible'),('zPQ-0582','Camión',12.75,'En Mantenimiento');
/*!40000 ALTER TABLE `vehiculos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'logisticatransportes'
--

--
-- Dumping routines for database 'logisticatransportes'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-23 11:56:29
