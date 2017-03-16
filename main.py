import sys

from PyQt5 import QtWidgets

from windows.connect_to_aws import ConnectToAws


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = ConnectToAws()
    sys.exit(app.exec_())
