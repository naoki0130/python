import sys
import random as rd
import csv
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize, QTimer


class ExampleWidget(QWidget):
    q_num = 0
    Q = []
    correct = []
    incorrect = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(900, 600)
        self.move(300, 300)
        self.setWindowTitle("sample")

        # count_text
        self.Q_num = QLabel("", self)
        self.font = QFont()
        self.font.setPointSize(32)
        self.Q_num.setFont(self.font)
        self.Q_num.move(265, 50)

        # task_layout
        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap("figures/white.jpg"))

        self.label2 = QLabel(self)
        self.label2.setPixmap(QPixmap("figures/white.jpg"))

        self.label3 = QLabel(self)
        self.label3.setPixmap(QPixmap("figures/left.png"))

        self.label4 = QLabel(self)
        self.label4.setPixmap(QPixmap("figures/R.png"))

        # task画像更新
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_task)
        self.timer.timeout.connect(self.question)
        self.timer.start(1500)  # every 10,000 milliseconds

        # buttonの設定
        img = QPixmap("figures/m.jpg")
        self.button1 = QPushButton("")
        self.button1.setIcon(QIcon(img))
        self.button1.setIconSize(QSize(200, 200))
        self.button1.setShortcut(Qt.Key_Up)
        self.button1.clicked.connect(self.button_do1)

        img = QPixmap("figures/h.jpg")
        self.button2 = QPushButton("")
        self.button2.setIcon(QIcon(img))
        self.button2.setIconSize(QSize(200, 200))
        self.button2.setShortcut(Qt.Key_Down)
        self.button2.clicked.connect(self.button_do2)

        self.btn_save = QPushButton("保存", self)
        self.btn_save.clicked.connect(self.save_csv)
        self.btn_save.setShortcut(Qt.Key_Right)

        # レイアウト配置
        self.task1 = QVBoxLayout()
        self.task1.addSpacing(100)
        self.task1.addWidget(self.label1, alignment=(Qt.AlignRight))
        self.task1.addWidget(self.label3, alignment=(Qt.AlignTop | Qt.AlignRight))

        self.task2 = QVBoxLayout()
        self.task2.addSpacing(100)
        self.task2.addWidget(self.label2)
        self.task2.addWidget(self.label4, alignment=(Qt.AlignTop))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button1, alignment=(Qt.AlignBottom))
        self.layout.addWidget(self.button2, alignment=(Qt.AlignTop))
        self.layout.addWidget(self.btn_save)

        self.task_all = QHBoxLayout()
        self.task_all.addLayout(self.task1)
        self.task_all.addLayout(self.task2)
        self.task_all.addLayout(self.layout)
        self.setLayout(self.task_all)

        # 表示
        self.show()

    def button_do1(self):
        self.correct.append(self.q_num)

    def button_do2(self):
        self.incorrect.append(self.q_num)

    def update_task(self):

        rd_lr = rd.randint(1, 100)
        rd_LR = rd.randint(1, 100)

        if rd_lr % 2 == 0:
            if rd_LR % 2 == 0:
                new_label1 = QPixmap("figures/task_L.jpg")
                self.label1.setPixmap(new_label1)
                new_label2 = QPixmap("figures/white.jpg")
                self.label2.setPixmap(new_label2)
                self.Q.append("left_L_correct")
            else:
                new_label1 = QPixmap("figures/task_R.jpg")
                self.label1.setPixmap(new_label1)
                new_label2 = QPixmap("figures/white.jpg")
                self.label2.setPixmap(new_label2)
                self.Q.append("left_R_incorrect")
        else:
            if rd_LR % 2 == 0:
                new_label2 = QPixmap("figures/task_L.jpg")
                self.label2.setPixmap(new_label2)
                new_label1 = QPixmap("figures/white.jpg")
                self.label1.setPixmap(new_label1)
                self.Q.append("right_L_incorrect")
            else:
                new_label2 = QPixmap("figures/task_R.jpg")
                self.label2.setPixmap(new_label2)
                new_label1 = QPixmap("figures/white.jpg")
                self.label1.setPixmap(new_label1)
                self.Q.append("right_R_correct")

    def question(self):
        self.q_num += 1
        self.Q_num.setText("Q：" + str(self.q_num))

    def save_csv(self):
        with open("Q.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.Q)
        with open("correct.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.correct)
        with open("incorrect.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.incorrect)
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ew = ExampleWidget()
    sys.exit(app.exec_())
