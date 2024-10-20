
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ejercicio 4")

        # Lista para almacenar las características de 3 mascotas
        self.mascotas = []

        # Widget central
        central = QWidget()

        # Creamos los layouts
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()

        # Creamos los widgets
        self.editName = QLineEdit("Introduce el nombre")
        self.editRaza = QLineEdit("Introduce la raza")
        self.editAge = QLineEdit("Introduce la edad")
        self.labelname = QLabel("Mascota 1: ")
        self.labelAge = QLabel("Mascota 2: ")
        self.labelRaza = QLabel("Mascota 3: ")
        self.boton = QPushButton("Agregar mascota")

        # Conectando el botón con el método para asignar y mostrar datos
        self.boton.clicked.connect(self.AsignarALbL)

        # Agregar widgets al layout
        hlayout1.addWidget(self.editName)
        hlayout1.addWidget(self.editRaza)
        hlayout1.addWidget(self.editAge)
        hlayout1.addWidget(self.boton)
        vlayout.addWidget(self.labelname)
        vlayout.addWidget(self.labelAge)
        vlayout.addWidget(self.labelRaza)

        # Agregar el layout horizontal al vertical
        vlayout.addLayout(hlayout1)

        # Configurar el layout principal
        central.setLayout(vlayout)
        self.setCentralWidget(central)

    def AsignarALbL(self):
        # Obtener los datos del QLineEdit
        name = self.editName.text()
        age = self.editAge.text()
        raza = self.editRaza.text()

        # Verificar si ya hay 3 mascotas
        if len(self.mascotas) < 3:
            # Agregar los datos como un diccionario a la lista
            self.mascotas.append({"nombre": name, "edad": age, "raza": raza})

            # Mostrar las mascotas almacenadas
            self.mostrarMascotas()

        else:
            # Si ya hay 3 mascotas, deshabilitar el botón
            self.boton.setDisabled(True)

    def mostrarMascotas(self):
        # Mostrar las características de las mascotas en los labels
        if len(self.mascotas) > 0:
            self.labelname.setText(f"Mascota 1: {self.mascotas[0]['nombre']}, {self.mascotas[0]['edad']} años, Raza: {self.mascotas[0]['raza']}")
        if len(self.mascotas) > 1:
            self.labelAge.setText(f"Mascota 2: {self.mascotas[1]['nombre']}, {self.mascotas[1]['edad']} años, Raza: {self.mascotas[1]['raza']}")
        if len(self.mascotas) > 2:
            self.labelRaza.setText(f"Mascota 3: {self.mascotas[2]['nombre']}, {self.mascotas[2]['edad']} años, Raza: {self.mascotas[2]['raza']}")
        

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()
import sys

class mainwindow(QMainWindow):
    def __init__(self):                                                                                                                                                                                                                                                                     
        super().__init__()
        self.setWindowTitle("Ejercicio 4")

        # Lista para almacenar las características de 3 mascotas
        self.mascotas = []

        # Widget central
        central = QWidget()

        # Creamos los layouts
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()

        # Creamos los widgets
        self.editName = QLineEdit("Introduce el nombre")
        self.editRaza = QLineEdit("Introduce la raza")
        self.editAge = QLineEdit("Introduce la edad")
        self.labelname = QLabel("Mascota 1: ")
        self.labelAge = QLabel("Mascota 2: ")
        self.labelRaza = QLabel("Mascota 3: ")
        self.boton = QPushButton("Agregar mascota")

        # Conectando el botón con el método para asignar y mostrar datos
        self.boton.clicked.connect(self.AsignarALbL)

        # Agregar widgets al layout
        hlayout1.addWidget(self.editName)
        hlayout1.addWidget(self.editRaza)
        hlayout1.addWidget(self.editAge)
        hlayout1.addWidget(self.boton)
        vlayout.addWidget(self.labelname)
        vlayout.addWidget(self.labelAge)
        vlayout.addWidget(self.labelRaza)

        # Agregar el layout horizontal al vertical
        vlayout.addLayout(hlayout1)

        # Configurar el layout principal
        central.setLayout(vlayout)
        self.setCentralWidget(central)

    def AsignarALbL(self):
        # Obtener los datos del QLineEdit
        name = self.editName.text()
        age = self.editAge.text()
        raza = self.editRaza.text()

        # Verificar si ya hay 3 mascotas
        if len(self.mascotas) < 3:
            # Agregar los datos como un diccionario a la lista
            self.mascotas.append({"nombre": name, "edad": age, "raza": raza})

            # Mostrar las mascotas almacenadas
            self.mostrarMascotas()

        else:
            # Si ya hay 3 mascotas, deshabilitar el botón
            self.boton.setDisabled(True)

    def mostrarMascotas(self):
        # Mostrar las características de las mascotas en los labels
        if len(self.mascotas) > 0:
            self.labelname.setText(f"Mascota 1: {self.mascotas[0]['nombre']}, {self.mascotas[0]['edad']} años, Raza: {self.mascotas[0]['raza']}")
        if len(self.mascotas) > 1:
            self.labelAge.setText(f"Mascota 2: {self.mascotas[1]['nombre']}, {self.mascotas[1]['edad']} años, Raza: {self.mascotas[1]['raza']}")
        if len(self.mascotas) > 2:
            self.labelRaza.setText(f"Mascota 3: {self.mascotas[2]['nombre']}, {self.mascotas[2]['edad']} años, Raza: {self.mascotas[2]['raza']}")
        

app = QApplication(sys.argv)