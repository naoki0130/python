import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QHBoxLayout)
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class mainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1300, 1000)
        #self.move(300, 300)
        self.setWindowTitle("sample")

        #figuresの設定
        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap("figures\white.jpg"))
        #self.label1.move(150, 250)

        self.label2 = QLabel(self)
        self.label2.setPixmap(QPixmap("figures\white.jpg"))
        #self.label2.move(450, 250)
        
        self.label3 = QLabel(self)
        self.label3.setPixmap(QPixmap("figures\left.png"))
        #self.label3.move(200, 600)

        self.label4 = QLabel(self)
        self.label4.setPixmap(QPixmap("figures\R.png"))
        #self.label4.move(490, 600)

        #buttonとfiguresの設定
        img_m = QPixmap("figures\m.jpg")
        self.button1 = QPushButton("")
        self.button1.setIcon(QIcon(img_m))
        self.button1.setIconSize(QSize(200, 200))

        img_b = QPixmap("figures\h.jpg")
        self.button2 = QPushButton("")
        self.button2.setIcon(QIcon(img_b))
        self.button2.setIconSize(QSize(200, 200))

        #main_layout
        self.q = QHBoxLayout()

        #sub_layout
        self.layout1 = QVBoxLayout()
        self.layout1.addSpacing(200)
        self.layout1.addWidget(self.label1, alignment=(Qt.AlignBottom|Qt.AlignRight))
        self.layout1.addWidget(self.label3, alignment=(Qt.AlignTop|Qt.AlignRight))

        self.layout2 = QVBoxLayout()
        self.layout2.addSpacing(200)
        self.layout2.addWidget(self.label2, alignment=(Qt.AlignBottom|Qt.AlignLeft))
        self.layout2.addWidget(self.label4, alignment=(Qt.AlignTop | Qt.AlignLeft))
        
        self.layout3 = QVBoxLayout()
        self.layout3.addSpacing(200)
        self.layout3.addWidget(self.button1, alignment=(Qt.AlignBottom))
        self.layout3.addSpacing(30)
        self.layout3.addWidget(self.button2, alignment=(Qt.AlignTop))
        self.layout3.addSpacing(200)

        self.q.addLayout(self.layout1)
        self.q.addLayout(self.layout2)
        self.q.addLayout(self.layout3)
        self.q.addSpacing(150)

        self.setLayout(self.q)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = mainWidget()
    sys.exit(app.exec_())