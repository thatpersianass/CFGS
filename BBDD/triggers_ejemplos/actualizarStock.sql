DELIMITER $$
CREATE TRIGGER actualizar_stock
AFTER INSERT ON Ventas
FOR EACH ROW
BEGIN
    UPDATE Productos 
    SET stock = stock - NEW.cantidad 
    WHERE id_pro = NEW.id_producto AND stock >= NEW.cantidad;
END $$
DELIMITER ;