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
        matricula_id = self.lnEdit_Matricula.text()

        if matricula_id.strip() == "":
            QMessageBox.information(self, "Error", "Por favor, ingrese un número de matrícula.")
            return

        for matricula in self.lst_matriculas:
            if matricula.id_matricula == matricula_id:
                self.lnEdit_Nombre.setText(matricula.nombre)
                self.lnEdit_Apellidos.setText(matricula.apellidos)
                self.lnEdit_Curso.setText(matricula.curso)
                self.lnEdit_Ciclo.setText(matricula.ciclo)

                if matricula.sexo == "Masculino":
                    self.rad_Masculino.setChecked(True)
                    self.rad_Femenino.setChecked(False)
                elif matricula.sexo == "Femenino":
                    self.rad_Femenino.setChecked(True)
                    self.rad_Masculino.setChecked(False)

                self.check_Estudia.setChecked("Estudia" in matricula.situacion)
                self.check_Trabaja.setChecked("Trabaja" in matricula.situacion)

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

                self.btn_Modificar.setText("Modificar")
                self.btn_Borrar.setText("Borrar")

                self.btn_Modificar.setEnabled(True)
                self.btn_Borrar.setEnabled(True)

                self.lnEdit_Matricula.setEnabled(False)
                self.btn_Buscar.setEnabled(False)

                return

        QMessageBox.information(self, "Resultado", f"No se encontró la matrícula con ID {matricula_id}.")
        self.matriculaNueva()
        
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
        self.lnEdit_Nombre.clear()
        self.lnEdit_Apellidos.clear()
        self.lnEdit_Curso.clear()
        self.lnEdit_Ciclo.clear()
        self.rad_Femenino.setChecked(False)
        self.rad_Masculino.setChecked(True)
        self.check_Estudia.setChecked(False)
        self.check_Trabaja.setChecked(False)

        self.lnEdit_Matricula.setEnabled(False)
        self.btn_Buscar.setEnabled(False)
    
    def btnBorrar(self):
        if not self.nw_matricula:
            matricula_id = self.lnEdit_Matricula.text()

            for matricula in self.lst_matriculas:
                if matricula.id_matricula == matricula_id:
                    respuesta = QMessageBox.question(self, "Confirmar eliminación", 
                                                    f"¿Estás seguro de que deseas eliminar la matrícula con ID {matricula_id}?",
                                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    
                    if respuesta == QMessageBox.Yes:
                        self.lst_matriculas.remove(matricula)

                        QMessageBox.information(self, "Éxito", f"La matrícula con ID {matricula_id} ha sido eliminada correctamente.")
                        self.btn_Borrar.setText("Cancelar")
                        self.btn_Borrar.setEnabled(False)
                        self.btn_Modificar.setEnabled(False)
                        self.lnEdit_Nombre.setEnabled(False)
                        self.lnEdit_Apellidos.setEnabled(False)
                        self.lnEdit_Curso.setEnabled(False)
                        self.lnEdit_Ciclo.setEnabled(False)
                        self.vertLay_Sexo.setEnabled(False)
                        self.vertLay_Situacion.setEnabled(False)
                        self.lnEdit_Matricula.clear()
                        self.lnEdit_Nombre.clear()
                        self.lnEdit_Apellidos.clear()
                        self.lnEdit_Curso.clear()
                        self.lnEdit_Ciclo.clear()
                        self.rad_Femenino.setChecked(False)
                        self.rad_Masculino.setChecked(False)
                        self.check_Estudia.setChecked(False)
                        self.check_Trabaja.setChecked(False)
                        self.lnEdit_Matricula.setEnabled(True)
                        self.btn_Buscar.setEnabled(True)
                        self.nw_matricula = False
                    return
        else:
            self.btn_Borrar.setText("Cancelar")
            self.btn_Borrar.setEnabled(False)
            self.btn_Modificar.setEnabled(False)
            self.lnEdit_Nombre.setEnabled(False)
            self.lnEdit_Apellidos.setEnabled(False)
            self.lnEdit_Curso.setEnabled(False)
            self.lnEdit_Ciclo.setEnabled(False)
            self.vertLay_Sexo.setEnabled(False)
            self.vertLay_Situacion.setEnabled(False)
            self.lnEdit_Matricula.clear()
            self.lnEdit_Nombre.clear()
            self.lnEdit_Apellidos.clear()
            self.lnEdit_Curso.clear()
            self.lnEdit_Ciclo.clear()
            self.rad_Femenino.setChecked(False)
            self.rad_Masculino.setChecked(False)
            self.check_Estudia.setChecked(False)
            self.check_Trabaja.setChecked(False)
            self.lnEdit_Matricula.setEnabled(True)
            self.btn_Buscar.setEnabled(True)
            self.nw_matricula = False
            
    def btnModificar(self):
        '''
        AL PRESIONAR BTN_MODIFICAR SE VERIFICA EN QUÉ ESTADO ESTÁ LA VENTANA Y SE REALIZA LA ACCIÓN NECESARIA
        '''
        if not self.nw_matricula:
            matricula_id = self.lnEdit_Matricula.text()

            for matricula in self.lst_matriculas:
                if matricula.id_matricula == matricula_id:
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
                    matricula.nombre = nombre
                    matricula.apellidos = apellidos
                    matricula.curso = curso
                    matricula.ciclo = ciclo
                    matricula.sexo = sexo
                    matricula.situacion = situacion

                    QMessageBox.information(self, "Éxito", f"La matrícula con ID {matricula_id} ha sido modificada correctamente.")
                    self.btn_Borrar.setText("Cancelar")
                    self.btn_Borrar.setEnabled(False)
                    self.btn_Modificar.setEnabled(False)
                    self.lnEdit_Nombre.setEnabled(False)
                    self.lnEdit_Apellidos.setEnabled(False)
                    self.lnEdit_Curso.setEnabled(False)
                    self.lnEdit_Ciclo.setEnabled(False)
                    self.vertLay_Sexo.setEnabled(False)
                    self.vertLay_Situacion.setEnabled(False)
                    self.lnEdit_Matricula.clear()
                    self.lnEdit_Nombre.clear()
                    self.lnEdit_Apellidos.clear()
                    self.lnEdit_Curso.clear()
                    self.lnEdit_Ciclo.clear()
                    self.rad_Femenino.setChecked(False)
                    self.rad_Masculino.setChecked(False)
                    self.check_Estudia.setChecked(False)
                    self.check_Trabaja.setChecked(False)
                    self.rad_Femenino.setEnabled(False)
                    self.rad_Masculino.setEnabled(False)
                    self.check_Estudia.setEnabled(False)
                    self.check_Trabaja.setEnabled(False)
                    self.lnEdit_Matricula.setEnabled(True)
                    self.btn_Buscar.setEnabled(True)
                    self.nw_matricula = False
                    return

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
                self.btn_Borrar.setText("Cancelar")
                self.btn_Borrar.setEnabled(False)
                self.btn_Modificar.setEnabled(False)
                self.lnEdit_Nombre.setEnabled(False)
                self.lnEdit_Apellidos.setEnabled(False)
                self.lnEdit_Curso.setEnabled(False)
                self.lnEdit_Ciclo.setEnabled(False)
                self.vertLay_Sexo.setEnabled(False)
                self.vertLay_Situacion.setEnabled(False)
                self.lnEdit_Matricula.clear()
                self.lnEdit_Nombre.clear()
                self.lnEdit_Apellidos.clear()
                self.lnEdit_Curso.clear()
                self.lnEdit_Ciclo.clear()
                self.rad_Femenino.setChecked(False)
                self.rad_Masculino.setChecked(False)
                self.check_Estudia.setChecked(False)
                self.check_Trabaja.setChecked(False)
                self.rad_Femenino.setEnabled(False)
                self.rad_Masculino.setEnabled(False)
                self.check_Estudia.setEnabled(False)
                self.check_Trabaja.setEnabled(False)
                self.lnEdit_Matricula.setEnabled(True)
                self.btn_Buscar.setEnabled(True)
                self.nw_matricula = False

            else:
                QMessageBox.information(self, "Error", "Todos los campos son obligatorios.")

# Ejecucion de la ventana
def main():
    app = QApplication(sys.argv) # o [] si no hay paso de argumentoss
    window = ClaseVentana()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
