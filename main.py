import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 250, 500, 500)
        self.setMaximumSize(500, 500)
        self.name = 'files/taxi.png'
        self.car = QPixmap(self.name)
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 75, 75)
        self.label.setPixmap(self.car)
        self.setMouseTracking(True)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self.name == 'files/taxi.png':
                self.name = 'files/police.png'
                self.car = QPixmap(self.name)
                self.label.setPixmap(self.car)
                self.update()
            else:
                self.name = 'files/taxi.png'
                self.car = QPixmap(self.name)
                self.label.setPixmap(self.car)
                self.update()

    def mouseMoveEvent(self, event):
        if not ((event.x() + 100 > 500) or (event.y() + 100 > 500)):
            self.label.setGeometry(event.x(), event.y(), 100, 100)
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    sys.exit(app.exec())