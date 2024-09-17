from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout)
import sys
class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ejercicio 5")

        # Lista para almacenar las características 
        self.caracteristicas = []

        # Widget central
        central = QWidget()

        # Creamos los layouts
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()

        # Creamos los widgets
        self.editCaract = QLineEdit("Introduce la caracteristica")
        self.label = QLabel("Caracteristicas: ")
        self.labelCaract = QLabel()
        self.boton = QPushButton("Agregar Caracteristica")

        # Conectando el botón con el método para asignar y mostrar datos
        self.boton.clicked.connect(self.AsignarALbL)

        # Agregar widgets al layout
        hlayout1.addWidget(self.editCaract)
        hlayout1.addWidget(self.boton)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.labelCaract)


        # Agregar el layout horizontal al vertical
        vlayout.addLayout(hlayout1)

        # Configurar el layout principal
        central.setLayout(vlayout)
        self.setCentralWidget(central)

    def AsignarALbL(self):
        # Obtener los datos del QLineEdit
        Caract = self.editCaract.text()


        # Verificar si ya hay 10 caracteristicas
        if len(self.caracteristicas) <= 10:
            # Agregar los datos a la lista
            self.caracteristicas.append(Caract)
            

            # Mostrar las caracteristicas almacenadas
            self.mostrarCaracteristicas()

        else:
            # Si ya hay 10 caracteristicas, deshabilitar el botón
            self.boton.setDisabled(True)

    def mostrarCaracteristicas(self):
        # Crear un string con todas las características, separadas por un salto de línea
        texto_caracteristicas = "\n".join(self.caracteristicas)
        
        # Establecer el texto concatenado en el QLabel
        self.labelCaract.setText(texto_caracteristicas)
       
        

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()