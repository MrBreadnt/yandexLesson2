import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.circles = []

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        x, y = (self.width()//2, self.height()//2)
        for i in self.circles:
            qp.drawEllipse(QPoint(x, y), i, i)
        qp.end()

    def run(self):
        self.circles.append(randint(1, 300))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
