
import os

from classes import info
from classes.app import get_app
from windows.ui import main_window_ui

from PySide6.QtCore import Signal, QFile, QIODevice
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):

    # signals
    importFileSignal = Signal(str)  
    clearLoadedModelSignal = Signal()  # when the viewport's contents are cleared
    displayUpdatedSignal = Signal()  # when the 3d viewport is updated
    exportFileSignal = Signal(str)  # need to export the mesh
    viewChangedSignal = Signal(int)  # set the page for the viewwidget

    def __init__(self, *args):
        super().__init__(*args)

        self.initialized = False

        # TODO load user settings

        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO set keyboard shortcuts
        
        # TODO set theme
        # TODO set window variables (name, title, position in monitor) 

        # TODO connect signals
        # view signals send the new page's index
        self.ui.btn_import_view.pressed.connect(lambda: self.viewChangedSignal.emit(0))
        self.ui.btn_dicom_view.pressed.connect(lambda: self.viewChangedSignal.emit(1))
        self.ui.btn_export_view.pressed.connect(lambda: self.viewChangedSignal.emit(2))

        self.viewChangedSignal.connect(self.ui.viewswidget.setCurrentIndex)

        # TODO initialize models

        # show this window with resizing to ensure canvas is displayed properly
        self.showWithCanvas()  # shows and then resizes the window to properly display canvas
        self.initialized = True

    def showWithCanvas(self):
        # for the canvas widget to properly fit, we need to shrink the window slightly and then 
        # set it to the size as before
        size = [self.size().width(), self.size().height()]
        self.resize(size[0] - 1, size[1] - 1)  
        self.show()
        self.resize(size[0], size[1])
        
        



