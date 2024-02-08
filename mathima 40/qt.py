import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        label = QLabel('Hello, PyQt5!')

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)

        self.setWindowTitle('PyQt5 Example')
        self.setGeometry(100, 100, 300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec_())
