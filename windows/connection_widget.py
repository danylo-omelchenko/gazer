from windows.common import UiWidget


class ConnectionWidget(UiWidget):
    ui = 'resources/ui/connection_widget.ui'

    def __init__(
            self, on_edit=None, on_connect=None, on_remove=None, **kwargs):
        super().__init__(**kwargs)
        self.connection_id = None
        self.on_edit = on_edit
        self.on_connect = on_connect
        self.on_remove = on_remove

    def update_connection(self, connection):
        self.connection_id = connection.id
        self.name_lbl.setText(connection.name)

    def edit_btn_click(self):
        self.on_edit(self)

    def connect_btn_click(self):
        self.on_connect(self)

    def remove_btn_click(self):
        self.on_remove(self)
