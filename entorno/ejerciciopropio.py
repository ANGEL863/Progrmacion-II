
from PyQt5.QtWidgets import *
import sys

class CalcularPropina(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ejercico propio")

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta para el monto total de la cuenta
        self.bill_label = QLabel("Monto total de la cuenta:")
        layout.addWidget(self.bill_label)

        # Campo de texto para el monto total
        self.bill_edit = QLineEdit()
        layout.addWidget(self.bill_edit)

        # Etiqueta para el porcentaje de propina
        self.tip_label = QLabel("Porcentaje de propina:")
        layout.addWidget(self.tip_label)

        # Campo de texto para el porcentaje de propina
        self.tip_edit = QLineEdit()
        layout.addWidget(self.tip_edit)

        # Botón para calcular la propina
        calculate_button = QPushButton("Calcular")
        calculate_button.clicked.connect(self.calculate_tip)
        layout.addWidget(calculate_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Propina:")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_tip(self):
        try:
            bill_amount = float(self.bill_edit.text())
            tip_percentage = float(self.tip_edit.text())
            tip = bill_amount * (tip_percentage / 100)
            self.result_label.setText(f"Propina: ${tip:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingresa valores numéricos.")
app = QApplication([])
window = CalcularPropina()
window.show()
app.exec_()