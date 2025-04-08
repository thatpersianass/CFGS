import os
import sys

from PySide6.QtWidgets import *
from matriculacion_ui import Ui_Matriculacion

class ClaseVentana(QWidget, Ui_Matriculacion):
    def __init__(self, parent=None):
        super(ClaseVentana, self).__init__(parent)
        self.setupUi(self)
    
    lst_matriculas = []
    nw_matricula = False
    
    class Matriculas:
        def __init__(self, id_matricula, nombre, apellidos, curso, ciclo, sexo, situacion):
            '''
            CLASE QUE CONTIENE TODOS LOS DATOS DE UNA MATRICULA
            '''
            self.id_matricula = id_matricula
            self.nombre = nombre
            self.apellidos = apellidos
            self.curso = curso
            self.ciclo = ciclo
            self.sexo = sexo
            self.situacion = situacion
    
    def verificarMatricula(self):
        '''
        VERIFICAR SI LA MATRICULA EXISTE EN LA ESTRUCTURA DE DATOS
        '''
        self.id_matricula = self.lnEdit_Matricula.text()
        if len(self.id_matricula) != 0:
            if self.id_matricula in self.lst_matriculas:
                QMessageBox.information(self, "Resultado de Búsqueda", "La matrícula existe en la estructura de datos.")
                self.matriculaExistente()
            else:
                QMessageBox.information(self, "Resultado de Búsqueda", "La matrícula NO existe en la estructura de datos.")
                self.matriculaNueva()
        else:
            QMessageBox.information(self, "Error", "El campo Matricula no puede estar vacío.")
        
    def matriculaExistente(self):
        '''
        LA MATRICULA EXISTE EN LA ESTRUCTURA DE DATOS
        '''
        self.nw_matricula = False
        self.btn_Modificar.setEnabled(True)
        self.btn_Borrar.setEnabled(True)
        self.btn_Buscar.setEnabled(False)
        
    def matriculaNueva(self):
        '''
        LA MATRICULA NO EXISTE EN LA ESTRUCTURA DE DATOS
        '''
        self.nw_matricula = True
        self.btn_Borrar.setEnabled(True)
        self.btn_Borrar.setText("Cancelar")
        self.btn_Modificar.setEnabled(True)
        self.btn_Modificar.setText("Agregar")
        self.lnEdit_Nombre.setEnabled(True)
        self.lnEdit_Apellidos.setEnabled(True)
        self.lnEdit_Curso.setEnabled(True)
        self.lnEdit_Ciclo.setEnabled(True)
        self.vertLay_Sexo.setEnabled(True)
        self.vertLay_Situacion.setEnabled(True)
        self.rad_Femenino.setEnabled(True)
        self.rad_Masculino.setEnabled(True)
        self.check_Estudia.setEnabled(True)
        self.check_Trabaja.setEnabled(True)
        self.lnEdit_Matricula.setEnabled(False)
        self.btn_Buscar.setEnabled(False)
    
    def btnBorrar(self):
        '''
        AL PRESIONAR BTN_BORRAR SE VERIFICA EN QUÉ ESTADO ESTÁ LA VENTANA Y SE REALIZA LA ACCIÓN NECESARIA
        '''
        if not self.nw_matricula:
            print("nah")
        else:
            self.btn_Borrar.setEnabled(False)
            self.btn_Borrar.setText("Borrar")
            self.btn_Modificar.setEnabled(False)
            self.btn_Modificar.setText("Modificar")
            self.lnEdit_Nombre.setEnabled(False)
            self.lnEdit_Apellidos.setEnabled(False)
            self.lnEdit_Curso.setEnabled(False)
            self.lnEdit_Ciclo.setEnabled(False)
            self.vertLay_Sexo.setEnabled(False)
            self.vertLay_Situacion.setEnabled(False)
            self.rad_Femenino.setEnabled(False)
            self.rad_Masculino.setEnabled(False)
            self.check_Estudia.setEnabled(False)
            self.check_Trabaja.setEnabled(False)
            self.lnEdit_Matricula.setEnabled(True)
            self.lnEdit_Matricula.setText("")
            self.btn_Buscar.setEnabled(True)
    
    def btnModificar(self):
        '''
        AL PRESIONAR BTN_MODIFICAR SE VERIFICA EN QUÉ ESTADO ESTÁ LA VENTANA Y SE REALIZA LA ACCIÓN NECESARIA
        '''
        if not self.nw_matricula:
            print("nah")
        else:
            if self.lnEdit_Nombre.text() != "" and self.lnEdit_Apellidos.text() != "" and self.lnEdit_Curso.text() != "" and self.lnEdit_Ciclo.text() != "":
                nombre = self.lnEdit_Nombre.text()
                apellidos = self.lnEdit_Apellidos.text()
                ciclo = self.lnEdit_Ciclo.text()
                curso = self.lnEdit_Curso.text()
                
                if self.rad_Femenino.isChecked():
                    sexo = "Femenino"
                elif self.rad_Masculino.isChecked():
                    sexo = "Masculino"
                else:
                    sexo = "No especificado"

                situacion = []
                if self.check_Estudia.isChecked():
                    situacion.append("Estudia")
                if self.check_Trabaja.isChecked():
                    situacion.append("Trabaja")
                situacion = ", ".join(situacion) if situacion else "No especificado"

                id_matricula = self.lnEdit_Matricula.text()
                nueva_matricula = self.Matriculas(id_matricula, nombre, apellidos, curso, ciclo, sexo, situacion)

                self.lst_matriculas.append(nueva_matricula)

                QMessageBox.information(self, "Éxito", f"La matrícula con ID {id_matricula} ha sido agregada correctamente.")

            else:
                QMessageBox.information(self, "Error", "Todos los campos son obligatorios.")
        self.btn_Borrar()
    
    def agregarMatricula(self):
        '''
        AGREGA UNA MATRICULA A LA ESTRUCTURA DE DATOS
        '''
        if not self.nw_matricula:
            print("nah")
        else:
            print("Yuh uh")
    
    def modificarMatricula(self):
        '''
        MODIFICA UNA MATRICULA DE LA ESTRUCTURA DE DATOS
        '''
        if not self.nw_matricula:
            print("nah")
        else:
            print("Yuh uh")

# Ejecucion de la ventana
def main():
    app = QApplication(sys.argv) # o [] si no hay paso de argumentoss
    window = ClaseVentana()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
