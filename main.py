import avisoCantidad
import avisoDNI
import avisoDatos
import avisoEdad
import var,events
import venCalendar
import ventana
from ventana import *
import sys
from PyQt5 import QtWidgets
from datetime import datetime
import windowaviso

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = ventana.Ui_MainWindow()
        var.ui.setupUi(self)
        var.dlgCalendar = DialogCalendar()
        var.avisoEdad=DialogEdad()
        var.avisoCantidad=DialogCantidad()
        var.saldo=0
        var.avisoDatos=DialogDatos()
        var.avisoDNI=DialogDNI()
        var.ui.botonSalir_2.clicked.connect(events.Eventos.Salir)
        var.ui.fechaIcono.clicked.connect(events.Eventos.abrirCalendar)
        var.ui.dni.editingFinished.connect(events.Eventos.validarDni)
        var.ui.menuIngreso.buttonClicked.connect(events.Eventos.selOperacion)
        var.ui.botonAceptar.clicked.connect(events.Eventos.actualizarSaldo)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar,self).__init__()
        var.dlgCalendar=venCalendar.Ui_Dialog()
        var.dlgCalendar.setupUi(self)
        diaActual = datetime.now().day
        mesActual = datetime.now().month
        anoActual = datetime.now().year
        var.dlgCalendar.calendarWidget.setSelectedDate(QtCore.QDate(anoActual,mesActual,diaActual))
        var.dlgCalendar.calendarWidget.clicked.connect(events.Eventos.cargarFecha)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgSlr = windowaviso.Ui_Dialog()
        var.dlgSlr.setupUi(self)

class DialogEdad(QtWidgets.QDialog):
    def __init__(self):
        super(DialogEdad, self).__init__()
        var.avisoEdad = avisoEdad.Ui_Dialog()
        var.avisoEdad.setupUi(self)

class DialogDatos(QtWidgets.QDialog):
    def __init__(self):
        super(DialogDatos, self).__init__()
        var.avisoDatos = avisoDatos.Ui_Dialog()
        var.avisoDatos.setupUi(self)

class DialogCantidad(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCantidad, self).__init__()
        var.avisoCantidad = avisoCantidad.Ui_Dialog()
        var.avisoCantidad.setupUi(self)

class DialogDNI(QtWidgets.QDialog):
    def __init__(self):
        super(DialogDNI, self).__init__()
        var.avisoDNI = avisoDNI.Ui_Dialog()
        var.avisoDNI.setupUi(self)

if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    window.show()
    var.dlgSlr = DialogSalir()
    sys.exit(app.exec())
