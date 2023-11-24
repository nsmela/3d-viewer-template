from PySide6.QtWidgets import QMainWindow, QFileDialog
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

from classes import info
from classes.mesh.imports import read_3d_file
from classes.app import get_app
from windows.ui import main_window_ui
from windows.views.viewport import OrbitCameraViewer3d

import os


class MainWindow(QMainWindow):

    def actionImportMesh(self):
        filename = QFileDialog.getOpenFileName(self, "Open model", "", "Model files (*.step *.stp *.stl);; All files (*.*))", "")[0]
        if not filename:  # no file selected?
            return
        
        shape = read_3d_file(filename=filename)
        self.app.signals.loadMesh.emit(shape)


    def __init__(self, *args):
        super().__init__(*args)

        app = get_app()
        self.initialized = False

        # TODO load user settings

        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO set keyboard shortcuts
        
        # TODO set theme
        # TODO set window variables (name, title, position in monitor) 

        # TODO connect signals to events
        # view signals send the new page's index
        self.ui.btn_import_view.pressed.connect(lambda: app.signals.viewChanged.emit(0))
        self.ui.btn_dicom_view.pressed.connect(lambda: app.signals.viewChanged.emit(1))
        self.ui.btn_export_view.pressed.connect(lambda: app.signals.viewChanged.emit(2))

        app.signals.viewChanged.connect(self.ui.viewswidget.setCurrentIndex)

        self.ui.btn_import_mesh.pressed.connect(self.actionImportMesh)

        # TODO initialize models

        # initialize canvas
        self.canvas = OrbitCameraViewer3d()
        self.ui.displayviewwidget.layout().addWidget(self.canvas)
        self.canvas.InitDriver()
        self.display = self.canvas._display
        a_box = BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape()
        self.ais_box = self.display.DisplayShape(a_box)[0]
        self.display.display_triedron()
        self.display.FitAll()

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
        
        



