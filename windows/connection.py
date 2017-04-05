from windows.common import UiWindow


class ConnectionWindow(UiWindow):
    ui = 'resources/ui/new_connection.ui'

    def __init__(self, title, init_data=None):
        super().__init__()
        self.setWindowTitle(title)
