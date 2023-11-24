
from PySide6.QtWidgets import QApplication

from classes.signals import AppSignals


def get_app():
    """ Returns the current QApplication instance """
    return QApplication.instance()


class RadiotherapyApp(QApplication):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = super().arguments()
        self.errors = []
        self.signals = AppSignals()

        try:
            from classes import info
            # TODO initialize logger

        except ImportError:
            # TODO log
            # stop launching
            raise
        
        # TODO log start

        self.path = info.DIR_PATH

    def gui(self):
        """
        Initialize the GUI and the Main Window
        :return: bool: True if the GUI has no errors, False if initialization fails
        """

        from windows.main_window import MainWindow
        # TODO log creating window
        self.window = MainWindow()

        # process args like autoloading a file or project


        return True

