
import os

from classes import info
from classes.app import get_app

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):

    # path -> ui file
    UI_PATH = os.path.join(info.DIR_PATH, "windows", "ui", "main-window.ui")

    # signals
    importFileSignal = Signal(str) 
    clearLoadedModelSignal = Signal()
    displayUpdatedSignal = Signal()

    def __init__(self, *args):
        super().__init__(*args)
        
        app = get_app()
        app.window = self

        

