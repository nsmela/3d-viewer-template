import unittest, sys
from pathlib import Path

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere

from src.classes.mesh.fileio import read_3d_file, write_3d_file

file_folder = Path(__file__).parent.joinpath("files")

shapes_file = file_folder.joinpath("shapes.step")
invalid_shape_file = file_folder.joinpath("invalid_shape.step")
invalid_file_type = file_folder.joinpath("invalid_file_type.bad")
not_found_file = file_folder.joinpath("nonsense.step")

export_stl_file = file_folder.joinpath("export.stl")
export_stp_file = file_folder.joinpath("export.stp")
export_step_file = file_folder.joinpath("export.step")
export_invalid_file_type = file_folder.joinpath("export.bad")


class TestRead3dFile(unittest.TestCase):

    def setUp(self):
        # delete the files if they exist
        # dont raise FileNotFound if they do not exist
        export_step_file.unlink(True)
        export_stl_file.unlink(True)        
        export_stp_file.unlink(True)

    def test_file_not_found(self):
        self.assertRaises(FileNotFoundError, read_3d_file, not_found_file)

    def test_invalid_shape_file(self):
        self.assertRaises(AssertionError, read_3d_file, invalid_shape_file)

    def test_invalid_file_type(self):
        self.assertRaises(AssertionError, read_3d_file, invalid_file_type)

    def test_output_type(self):
        from OCC.Core.TopoDS import TopoDS_Compound
        self.assertIsInstance(read_3d_file(shapes_file), TopoDS_Compound)

    def test_export_file(self):
        test_shape = BRepPrimAPI_MakeSphere(10.0).Solid()

        with self.subTest():
            self.assertRaises(AssertionError, write_3d_file, export_invalid_file_type, test_shape)

        write_3d_file(export_step_file, test_shape)
        with self.subTest():
            self.assertEqual(export_step_file.exists(), True, "no step file generated")

        write_3d_file(filename=export_stl_file, shape=test_shape)
        with self.subTest():
            self.assertEqual(export_stl_file.exists(), True, "no stl file generated")

        write_3d_file(export_stp_file, test_shape)
        with self.subTest():
            self.assertEqual(export_stp_file.exists(), True, "no stp file generated")

    def tearDown(self):
        # delete the files if they exist
        # dont raise FileNotFound if they do not exist
        export_step_file.unlink(True)
        export_stl_file.unlink(True)        
        export_stp_file.unlink(True)
