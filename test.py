# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        btn1 = QtGui.QPushButton('Button1', self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton('Button2', self)
        btn2.move(150, 50)

        # 将两个按钮关联到相同的槽（slot）。
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        
        self.checkInTime = QtGui.QTimeEdit(self)
        self.checkInTime.setGeometry(QtCore.QRect(107, 31, 121, 31))
        self.checkInTime.setObjectName("checkInTime")
        self.checkInTime.setMinimumTime(QtCore.QTime(8, 10, 0))
        self.checkInTime.setMaximumTime(QtCore.QTime(8, 30, 0))
        
        self.checkInTime.timeChanged.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event handler')
        self.show()

    # 通过调用sender()方法判断信号源。
    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()