import webbrowser

from windows.common import UiWindow
from windows.connection import ConnectionWindow
from windows.info import InfoWindow


class StartWindow(UiWindow):
    ui = 'resources/ui/start.ui'

    def add_new_connection(self):
        self.connection_edit_window = ConnectionWindow('Add New Connection')
        self.connection_edit_window.show()

    def show_info(self):
        self.info_dialog = InfoWindow()
        self.info_dialog.show()

    def show_github(self):
        webbrowser.open('https://github.com/daniil-omelchenko/gazer')
