
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
            from classes import info, logger
            logger.log.info(f"Starting {info.APP_NAME}")

        except ImportError:
            # TODO log
            # stop launching
            raise

        except Exception as error_message:
            print(f"unable to start logging. {error_message}")
            raise

        self.path = info.DIR_PATH

    def gui(self):
        """
        Initialize the GUI and the Main Window
        :return: bool: True if the GUI has no errors, False if initialization fails
        """

        try:
            from windows.main_window import MainWindow
            self.window = MainWindow()

            # TODO process args like autoloading a file or project

            return True
        
        except Exception as error_message:
            from classes import logger
            logger.log.critical(f"Main window start failed: {error_message}")
            return False

