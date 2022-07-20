import os
import sys

from PyQt5 import QtCore, QtWidgets, uic

from QTThreading import DoThreading
from CustomQtWidgets import CustomQtWidgets

main_path = ""


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        is_close = CustomQtWidgets.do_get_question(
            self, "Quit", "Are you sure want to quit?"
        )

        if is_close:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


class MainWindow(Window):
    def __init__(self, ui_path):
        super().__init__()
        uic.loadUi(os.path.join(main_path, ui_path), self)
        self.setFixedSize(self.size())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.center()
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow("MainWindow.ui")
    app.exec_()
