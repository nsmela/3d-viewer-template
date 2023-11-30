from PySide6.QtWidgets import QMainWindow, QFileDialog

from src.classes.logger import log
from src.classes.mesh.fileio import read_3d_file
from src.classes.app import get_app
from src.windows.ui import main_window_ui
from src.windows.views.viewport import OrbitCameraViewer3d
from src.windows.models.displaymodel import DisplayModel
from src.windows.models.shapemodel import ShapeModel

class MainWindow(QMainWindow):

    def actionImportMesh(self):
        filename = QFileDialog.getOpenFileName(self, "Open model", "", "Model files (*.step *.stp *.stl);; All files (*.*))", "")[0]
        
        if not filename:  # no file selected?
            log.info("no valid filename selected for importing")
            return
        
        log.info(f"file {filename} has been selected")

        shape = read_3d_file(filename=filename)
        shape_model = ShapeModel("main", shape)
        self.displaymodel.add_shape(shape_model)

    def actionTestMultipleShapes(self):
        from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere
        from OCC.Core.gp import gp_Pnt
        from random import randint

        amount = 10

        log.info(f"Adding {amount} spheres to the viewer for testing")
        label = "test_sphere"
        shapes = []
        for i in range(amount):
            point = gp_Pnt(randint(-30, 30), randint(-30, 30), 0)
            shape = BRepPrimAPI_MakeSphere(point, randint(5, 10)).Shape()
            shape_model = ShapeModel(label=f"{label}_{i}", shape=shape, rgb=(0.1, randint(0, 10) / 10, 0.9))
            shapes.append(shape_model)
        self.displaymodel.add_shapes(shapes)

    def actionTestRemoveShape(self):
        from random import randint
    
        shapes = list(self.displaymodel.shapes.values())
        if len(shapes) < 1: return

        label = shapes[randint(0, len(shapes) - 1)].label
        self.displaymodel.remove_shape(label)

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

        self.ui.btn_import_mesh.pressed.connect(self.actionImportMesh)

        # TODO test buttons
        self.ui.btn_test_1.pressed.connect(self.actionTestMultipleShapes)
        self.ui.btn_test_2.pressed.connect(self.actionTestRemoveShape)

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
        
        



