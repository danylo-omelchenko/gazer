from PyQt5 import QtWidgets

import settings_manager
from windows.swf import SWFWindow


class ConnectToAws(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 300, 400, 150)

        self.aws_key_id_input = QtWidgets.QLineEdit()
        self.aws_secret_key_input = QtWidgets.QLineEdit()
        self.connect_button = QtWidgets.QPushButton('Connect')

        self.initialize_components()
        self.show()

    def initialize_components(self):
        settings = settings_manager.load_settings()
        v_box = QtWidgets.QVBoxLayout(self)

        self.aws_key_id_input.setPlaceholderText('ACCESS KEY ID')
        self.aws_key_id_input.setText(settings.get('aws_key_id', ''))
        v_box.addWidget(self.aws_key_id_input)

        self.aws_secret_key_input.setPlaceholderText('ACCESS SECRET KEY')
        self.aws_secret_key_input.setText(settings.get('aws_secret_key', ''))
        v_box.addWidget(self.aws_secret_key_input)

        self.connect_button.clicked.connect(self.connect_button_on_click)
        v_box.addWidget(self.connect_button)

    def connect_button_on_click(self):
        aws_key_id = self.aws_key_id_input.text()
        aws_secret_key = self.aws_secret_key_input.text()
        settings = {
            'aws_key_id': aws_key_id,
            'aws_secret_key': aws_secret_key}
        settings_manager.save_settings(settings)
        self.swf_window = SWFWindow('title')
