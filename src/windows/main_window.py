
import os

from classes import info
from classes.app import get_app
from .ui import main_window_ui

from PySide6.QtCore import Signal, QFile, QIODevice
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):

    # signals
    importFileSignal = Signal(str) 
    clearLoadedModelSignal = Signal()
    displayUpdatedSignal = Signal()
    exportFileSignal = Signal()  # need to export the mesh

    def __init__(self, *args):
        super().__init__(*args)

        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

    def showWithCanvas(self):
        # for the canvas widget to properly fit, we need to shrink the window slightly and then 
        # set it to the size as before
        size = [self.size().width(), self.size().height()]
        self.resize(size[0] - 1, size[1] - 1)  
        self.show()
        self.resize(size[0], size[1])
        
        



