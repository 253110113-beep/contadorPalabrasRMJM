import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # carga de nuestra vista
        uic.loadUi("ContadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.contarPalabras)

    def contarPalabras(self):
        # Recupera el texto (usa .toPlainText() si es QTextEdit)
        texto = self.editCaracteres.text()
        
        # Separa las palabras
        textoSeparado = texto.split()
        print(textoSeparado)  # Sin comillas para ver la lista real
        
        # Contar las palabras y caracteres
        num_palabras = len(textoSeparado)
        num_caracteres = len(texto)
        
        print("Se ha presionado el botón")
        print(f"Palabras: {num_palabras}")
        print(f"Caracteres: {num_caracteres}")

app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())