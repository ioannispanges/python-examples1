import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

app = QApplication(sys.argv)

window = QWidget()

label = QLabel('Hello')
button = QPushButton('Click me!')
line_edit = QLineEdit()

layout = QVBoxLayout()

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(line_edit)

window.setLayout(layout)

window.setWindowTitle('Example')

window.show()

sys.exit(app.exec_())
