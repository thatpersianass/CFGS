DELIMITER $$
CREATE TRIGGER auditoria_ventas
AFTER INSERT ON Ventas
FOR EACH ROW
BEGIN
    INSERT INTO Historial_auditoria (id_venta, evento, fecha_evento)
    VALUES (
        NEW.id_venta, 
        CONCAT('Venta del producto: ', NEW.cantidad, ' unidades del producto ID ', NEW.id_producto), 
        NOW()
    );
END $$