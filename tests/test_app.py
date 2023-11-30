import unittest
from src.classes.app import RadiotherapyApp


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = self.app = RadiotherapyApp()

    def test_app_gui(self):
        self.assertTrue(self.app.gui())

    def tearDown(self) -> None:
        del self.app
