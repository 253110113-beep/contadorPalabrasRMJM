import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # carga de nuestra vista
        uic.loadUi("ContadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.contarPalabras)

    def contarPalabras(self):
        # Recupera el texto 
        texto = self.editCaracteres.text()
        
        # Separa las palabras
        textoSeparado = texto.split()
        print(textoSeparado)  
        
        # Contar las palabras y caracteres
        cantidadPalabras = len (textoSeparado)
        print("Cantidad de palabras:", cantidadPalabras)
        num_palabras = len(textoSeparado)
        self.tvPalabras.setText(f'palabras:{cantidadPalabras}')
        num_caracteres = len(texto)
        totalCaracteres=0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        totalCaracteres
        self.tvCaracteres.setText(f'caracteres:{totalCaracteres}')
        
        print("Se ha presionado el botón")
        
        if cantidadPalabras >= 20:        
            self.tvPalabras.setStyleSheet("color: #ff0000;")
        else:
            self.tvPalabras.setStyleSheet("color: #ffffff;")
            
        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet("color: #ff0000;")
        else:
            self.tvCaracteres.setStyleSheet("color: #ffffff;")

app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())