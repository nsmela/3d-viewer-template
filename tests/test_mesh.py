import unittest

from src.classes.mesh.imports import read_3d_file


class TestRead3dFile(unittest.TestCase):
    def setUp(self) -> None:
        pass


    def test_input_exists(self):
        self.assertIsNotNone(self.my_message)

    def tearDown(self) -> None:
        pass

