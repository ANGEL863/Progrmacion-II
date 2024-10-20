
"""
Construir un programa que muestre una ventana 
y que lea una clave secreta sin mostrar los caracteres que la componen.

"""

from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("eercicio 2")
        self.setGeometry(100, 100, 300, 150)

        #widget central
        central = QWidget()

        #Creamos los layouts
        layout = QVBoxLayout()

        #creamos los widgets 
        self.lbl= QLabel("Introduce tu clave secreta: ")
        self.editPsw = QLineEdit()
        #echomode para ocultar
        self.editPsw.setEchoMode(QLineEdit.Password)
        self.button = QPushButton("Leer clave")
        self.lblResult = QLabel("")

        #signal del boton
        self.button.clicked.connect(self.showpsw)
        

        #agregar widgets al layout
        layout.addWidget(self.lbl)
        layout.addWidget(self.editPsw)
        layout.addWidget(self.button)
        layout.addWidget(self.lblResult)

        central.setLayout(layout)
        self.setCentralWidget(central)
    
    def showpsw (self):
        psw = self.editPsw.text()
        self.lblResult.setText("La clave secreta es: " + 2024)
        

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()