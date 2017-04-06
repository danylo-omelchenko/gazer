import sys

from PyQt5 import QtWidgets

import application
from windows.start import StartWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = StartWindow()
    application.main_window = main_window
    main_window.show()
    sys.exit(app.exec_())
