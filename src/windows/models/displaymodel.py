from PySide6.QtCore import QObject, Signal
from OCC.Core.TopoDS import TopoDS_Shape


class DisplayModel(QObject):

    shapes_changed = Signal(list, bool)

    def add_shape(self, label: str, shape: TopoDS_Shape):
        value = [label, shape]
        self.shapes.append(value)
        self.shapes_changed.emit(self.shapes, True)

    def __init__(self):
        super().__init__()

        self.shapes = []


