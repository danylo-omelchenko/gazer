import os
import sys

from PyQt5 import QtWidgets, uic


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class UiWindow(QtWidgets.QMainWindow):
    ui = None

    def __init__(self):
        super().__init__()
        if self.ui:
            uic.loadUi(resource_path(self.ui), self)
