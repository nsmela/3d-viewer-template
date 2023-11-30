import unittest

from tests import test_mesh

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_mesh))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)