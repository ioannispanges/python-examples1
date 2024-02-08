import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication(sys.argv)

windows = QWidget()
layout = QVBoxLayout()

label1 = QLabel('Widget 1')
label2 = QLabel('Widget 2')

layout.addWidget(label1)
layout.addWidget(label2)

windows.setLayout(layout)

windows.setWindowTitle('PyQt5 QVBoxLayout Example')
windows.setGeometry(100, 1000, 300, 200)

windows.show()

sys.exit(app.exec_())
