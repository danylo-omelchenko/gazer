from PyQt5 import QtWidgets


class SWFWindow(QtWidgets.QWidget):

    def __init__(self, title):
        super().__init__()
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle(str(title))

        self.open_file_dialog = QtWidgets.QFileDialog()
        self.open_button = QtWidgets.QPushButton('Open')
        self.v_box = QtWidgets.QVBoxLayout(self)

        self.initialize_components()

        self.show()

    def initialize_components(self):
        self.open_button.clicked.connect(self.open_button_clicked)
        self.v_box.addWidget(self.open_button)
        self.v_box.addStretch(2)

    def open_button_clicked(self):
        # print(self.open_file_dialog.getOpenFileNames())
        new_button = QtWidgets.QPushButton('New')
        self.v_box.addWidget(new_button)
