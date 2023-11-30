import unittest
from pathlib import Path

from src.classes.mesh.imports import read_3d_file

file_folder = Path(__file__).parent.joinpath("files")
shapes_file = file_folder.joinpath("shapes.step")
invalid_shape_file = file_folder.joinpath("invalid_shape.step")
invalid_file_type = file_folder.joinpath("invalid_file_type.bad")
not_found_file = file_folder.joinpath("nonsense.step")

class TestRead3dFile(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_not_found(self):
        self.assertRaises(FileNotFoundError, read_3d_file, not_found_file)

    def test_invalid_shape_file(self):
        self.assertRaises(AssertionError, read_3d_file, invalid_shape_file)

    def test_invalid_file_type(self):
        self.assertRaises(AssertionError, read_3d_file, invalid_file_type)

    def test_output_type(self):
        from OCC.Core.TopoDS import TopoDS_Compound
        self.assertIsInstance(read_3d_file(shapes_file), TopoDS_Compound)

    def tearDown(self) -> None:
        pass

