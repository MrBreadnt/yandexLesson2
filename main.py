import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.circles = []

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        x, y = (self.width() // 2, self.height() // 2)
        for i in self.circles:
            qp.setBrush(i[1])
            qp.drawEllipse(QPoint(x, y), i[0], i[0])
        qp.end()

    def run(self):
        self.circles.append((randint(1, 300), QColor(randint(0, 256), randint(0, 256), randint(0, 256))))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
