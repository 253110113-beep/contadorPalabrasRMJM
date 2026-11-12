import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # carga de nuestra vista
        uic.loadUi("ContadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.contarPalabras)

    def contarPalabras(self):
        #recupera el texto
        texto = self.editCaracteres.text()
        "separa las palabras"
        textoSeparado= texto.split()
        print("texto separado")
        #contar las palabras 
        #contar los caracteres 
        print("se ha presionado el boton")

app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()  # <-- Faltaban estos paréntesis
sys.exit(app.exec_())