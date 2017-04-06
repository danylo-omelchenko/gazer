import webbrowser
from functools import partial
import application
from windows.common import UiWindow
from windows.connection import ConnectionWindow
from windows.connection_widget import ConnectionWidget
from windows.info import InfoWindow


class StartWindow(UiWindow):
    ui = 'resources/ui/start.ui'

    def new_connection_btn_click(self):
        self.connection_edit_window = ConnectionWindow(
            'Add New Connection',
            on_success=self.add_new_connection)
        self.connection_edit_window.show()

    def add_new_connection(self, new_connection):
        application.context.connections.update(
            {new_connection.id: new_connection})
        connection_widget = ConnectionWidget(
            on_edit=self.edit_connection)
        connection_widget.update_connection(new_connection)
        layout = application.main_window.connections_bar_layout
        layout.insertWidget(layout.count() - 1, connection_widget)

    def save_connection(self, updated_connection, connection_widget):
        application.context.connections.update(
            {updated_connection.id: updated_connection})
        connection_widget.update_connection(updated_connection)

    def edit_connection(self, connection_widget):
        connection = application.context.connections.get(
            connection_widget.connection_id)
        self.connection_edit_window = ConnectionWindow(
            'Edit Connection',
            connection=connection,
            on_success=partial(
                self.save_connection,
                connection_widget=connection_widget))
        self.connection_edit_window.show()

    def info_btn_click(self):
        self.info_dialog = InfoWindow(self)
        self.info_dialog.show()

    def github_btn_click(self):
        webbrowser.open('https://github.com/daniil-omelchenko/gazer')
