import datetime
import sys
import var


class Eventos():

    def Salir(self):
        try:
            var.dlgSlr.show()
            if var.dlgSlr.exec():
                sys.exit()
            else:
                var.dlgSlr.hide()
        except Exception as error:
            print("Error: %s", str(error))

    def selOperacion(self):
        try:
            if var.ui.retirar.isChecked():
                var.operacion = False
            if var.ui.ingresar.isChecked():
                var.operacion = True
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)

    def validarDni():
        try:
            var.dniCorrecto=False
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            numeros = "1234567890"
            dni=var.ui.dni.text()
            if (len(dni) == 9):
                letraControl = dni[8].upper()
                dni = dni[:8]
                if (len(dni) == len([n for n in dni if n in numeros])):
                    if tabla[int(dni) % 23] == letraControl:
                        var.ui.label.setText('V')
                        var.ui.label.setStyleSheet('QLabel{color:green;font-size:14pt;font-weight:bold;}')
                        var.dniCorrecto=True

                    else:
                        var.ui.label.setStyleSheet('QLabel{color:red;font-size:14pt;font-weight:bold;}')
                        var.ui.label.setText('X')
            else:
                var.ui.label.setText('X')
                var.ui.label.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold;}')

        except Exception as error:
            print('Error en módulo validar DNI', error)

    def abrirCalendar():
        try:
            var.dlgCalendar.show()
        except Exception as error:
            print("Error en módulo de selección de fecha:", error)

    def cargarFecha(qDate):
        try:
            qfechaMinima=datetime.datetime.now() - datetime.timedelta(days=18 * 365)
            if qDate>qfechaMinima:
                var.avisoEdad.show()
                print("Lo siento, los menores de edad no pueden realizar operaciones")
                var.fechaValida=False
            else:
                data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
                var.ui.fecha.setText(str(data))
                var.fechaValida=True
            var.dlgCalendar.hide()

        except Exception as error:
            print("Error en módulo de selección de fecha:", error)

    def actualizarSaldo(self):
        try:
            cantidad = int(var.ui.cantidad.text())
            if var.fechaValida != True:
                print("Lo siento, los menores no pueden realizar operaciones")
            if var.dniCorrecto != True:
                print("Debe introducir un DNI correcto para continuar")
                var.avisoDNI.show()
            else:
                if var.operacion == True:
                    var.saldo += cantidad
                if var.operacion == False:
                    var.saldo-=cantidad
                var.ui.saldo.setText(str(var.saldo))
        except ValueError as error:
            var.avisoCantidad.show()
        except Exception as error:
            var.avisoDatos.show()






