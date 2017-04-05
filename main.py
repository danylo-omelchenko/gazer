import sys

from PyQt5 import QtWidgets

from windows.start import StartWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = StartWindow()
    gui.show()
    sys.exit(app.exec_())
