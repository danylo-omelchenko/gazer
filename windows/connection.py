from application import Connection
import config
import swf.utils
from windows.common import UiWindow


class ConnectionWindow(UiWindow):
    ui = 'resources/ui/new_connection.ui'

    def __init__(self, title, connection=None, on_success=None, **kwargs):
        super().__init__(**kwargs)
        self.connection = connection
        self.on_success = on_success
        self.setWindowTitle(title)
        self.load_default_data()
        self.load_from_context()

    def load_default_data(self):
        self.region_cmb.clear()
        self.region_cmb.addItems(
            [region.name for region in swf.utils.all_regions()])
        self.region_cmb.setCurrentIndex(
            self.region_cmb.findText(config.DEFAULT_REGION))

    def load_from_context(self):
        if self.connection:
            self.connection_name_txt.setText(self.connection.name)
            self.access_id_txt.setText(self.connection.aws_access_key_id)
            self.secret_key_txt.setText(self.connection.aws_secret_access_key)
            self.region_cmb.setCurrentIndex(
                self.region_cmb.findText(self.connection.region))

    def save_connection(self):
        connection = Connection(
            name=self.connection_name_txt.text(),
            aws_access_key_id=self.access_id_txt.text(),
            aws_secret_access_key=self.secret_key_txt.text(),
            region=self.region_cmb.currentText())
        self.on_success(connection)
        self.close()
