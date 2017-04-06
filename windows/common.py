import os
import sys

from PyQt5 import QtWidgets, uic


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class Ui:
    ui = None
    parent = None

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        if self.ui:
            uic.loadUi(resource_path(self.ui), self)


class UiWindow(QtWidgets.QMainWindow, Ui):
    pass


class UiWidget(QtWidgets.QWidget, Ui):
    pass
