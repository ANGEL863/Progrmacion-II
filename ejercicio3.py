
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout,QPushButton,QLineEdit)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ejercicio 3")

        #widget central
        central = QWidget()

        #Creamos los layouts
        vlayout = QVBoxLayout()

        #creamos los widgets 
        self.editName = QLineEdit("Introduce tu nombre completo")
        self.editID = QLineEdit("Introduce tu ID")
        self.labelname = QLabel()
        self.labelID = QLabel()
        boton = QPushButton("Haz click aqui")


        #Conectando el boton con los edit 
        boton.clicked.connect(self.AsignarALbL)

        #agregar widgets al layout
        vlayout.addWidget(self.editName)
        vlayout.addWidget(self.editID)
        vlayout.addWidget(boton)
        vlayout.addWidget(self.labelname)
        vlayout.addWidget(self.labelID)
        
        central.setLayout(vlayout)
        self.setCentralWidget(central)


    def AsignarALbL(self):
        name = self.editName.text()
        self.labelname.setText(name)
        ID = self.editID.text()
        self.labelID.setText(ID)
        

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()