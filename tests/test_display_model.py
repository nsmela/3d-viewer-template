import unittest
from pathlib import Path

from OCC.Core.gp import gp_Pnt
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere

from src.windows.models.displaymodel import DisplayModel, ShapeModel

file_folder = Path(__file__).parent.joinpath("files")
shapes_file = file_folder.joinpath("shapes.step")
invalid_shape_file = file_folder.joinpath("invalid_shape.step")
invalid_file_type = file_folder.joinpath("invalid_file_type.bad")
not_found_file = file_folder.joinpath("nonsense.step")


class TestDisplayModel(unittest.TestCase):

    # methods needed
    def response_slot(self, shapes: list, udpate: bool):
        self.response = shapes

    def setUp(self):
        self.model = DisplayModel()
        self.response = []
        self.model.shapes_changed.connect(self.response_slot)

    def test_add_shape(self):
        test_label = "test"
        test_sphere = BRepPrimAPI_MakeSphere(20.0)
        test_rgb = (1.0, 0.5, 1.0)
        shape_model = ShapeModel(test_label, test_sphere, test_rgb)
        self.model.add_shape(shape_model)

        # if asserted, ends the test
        self.assertEqual(len(self.response), 1, "Response didn't contain only 1 shape model")
        
        response_model = self.response.pop()

        # want to allow multiple assertions
        with self.subTest():
            self.assertEqual(response_model.label, test_label, "Shape Model label doesn't match")
        with self.subTest():
            self.assertEqual(response_model.shape, test_sphere, "Shape model shape doesn't match")
        with self.subTest():
            self.assertEqual(response_model.rgb, test_rgb, "Shape model rgb doesn't match")

    def test_remove_shape(self):
        test_label = "test"
        test_sphere = BRepPrimAPI_MakeSphere(20.0)
        test_rgb = (1.0, 0.5, 1.0)
        shape_model = ShapeModel(test_label, test_sphere, test_rgb)
        self.model.add_shape(shape_model)

        # if asserted, ends the test
        self.assertEqual(len(self.response), 1, "Unable to test remove_shape, no shape model loaded")

        self.model.remove_shape(test_label)

        self.assertEqual(len(self.response), 0, "Response isn't equal to zero")

    def test_set_colour(self):
        test_label = "test"
        test_sphere = BRepPrimAPI_MakeSphere(20.0)
        test_rgb = (1.0, 0.5, 1.0)
        shape_model = ShapeModel(test_label, test_sphere, test_rgb)
        self.model.add_shape(shape_model)

        # if asserted, ends the test
        self.assertEqual(len(self.response), 1, "Unable to test set_colour, no shape model loaded")

        test_colour = (0, 1, 0)
        self.model.set_shape_color({test_label: test_colour})

        response_model = self.response.pop()
        self.assertEqual(response_model.rgb, test_colour, "Response doesn't match new colour")

    def tearDown(self):
        self.model.shapes_changed.disconnect(self.response_slot)
