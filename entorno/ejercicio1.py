from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout,QHBoxLayout)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ejercicio 1")

        #widget central
        central = QWidget()

        #Creamos los layouts
        hlayout = QHBoxLayout()

        #creamos los widgets en este caso labels
        self.lblvacio= QLabel("")
        labelname = QLabel("Angel Sorto")
        labelage = QLabel("Edad: 21")

        #agregar widgets al layout
        hlayout.addWidget(self.lblvacio)
        hlayout.addWidget(labelname)
        hlayout.addWidget(labelage)
        hlayout.addWidget(self.lblvacio)

        central.setLayout(hlayout)
        self.setCentralWidget(central)
        

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()
