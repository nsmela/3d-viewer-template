import unittest

from tests import test_mesh, test_app, test_display_model

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_mesh))
suite.addTests(loader.loadTestsFromModule(test_app))
suite.addTests(loader.loadTestsFromModule(test_display_model))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)