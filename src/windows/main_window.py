from PySide6.QtWidgets import QMainWindow, QFileDialog

from OCC.Core.BRep import BRep_Builder

from classes.logger import log
from classes.mesh.fileio import read_3d_file, write_3d_file
from classes.app import get_app
from windows.ui import main_window_ui
from windows.views.viewport import OrbitCameraViewer3d
from windows.models.displaymodel import DisplayModel
from windows.views.mesh_view import Mesh_View
from windows.views.modify_view import Modify_View

class MainWindow(QMainWindow):

    def actionExportMesh(self):
        from OCC.Core.TopoDS import TopoDS_Compound
        filename = QFileDialog.getSaveFileName(
            self, "Save model", "", "BRep file (*.step *.stp);; STL File (*.stl);; All files (*.*))", "")

        if not filename:  # no file selected?
            log.info("no valid filename selected for importing")
            return
        
        log.info(f"file {filename} has been selected for exporting")

        compound = TopoDS_Compound()
        shape_tool = BRep_Builder()
        shape_tool.MakeCompound(compound)
        shapes = {sm: sm.shape for sm in self.displaymodel.shapes.values()}
        for shape in shapes.values():
            shape_tool.Add(compound, shape)

        write_3d_file(filename[0], compound)

    def __init__(self, *args):
        super().__init__(*args)

        app = get_app()
        self.initialized = False

        log.info("Starting main window initialization")

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

        #self.ui.btn_export_shapes.pressed.connect(self.actionExportMesh)

        # TODO initialize models
        self.displaymodel = DisplayModel()

        # initialize canvas
        self.canvas = OrbitCameraViewer3d()
        self.ui.displayviewwidget.layout().addWidget(self.canvas)
        self.canvas.InitDriver()
        self.display = self.canvas._display

        self.display.display_triedron()
        self.display.FitAll()

        self.displaymodel.shapes_changed.connect(self.canvas.update_display)

        # TODO views
        self.ui.page_mesh.layout().addWidget(Mesh_View())
        self.ui.page_modify.layout().addWidget(Modify_View())

        # show this window with resizing to ensure canvas is displayed properly
        self.showWithCanvas()  # shows and then resizes the window to properly display canvas
        self.initialized = True

        log.info("main window initialization complete")

    def showWithCanvas(self):
        # for the canvas widget to properly fit, we need to shrink the window slightly and then 
        # set it to the size as before
        size = [self.size().width(), self.size().height()]
        self.resize(size[0] - 1, size[1] - 1)  
        self.show()
        self.resize(size[0], size[1])
        
        



