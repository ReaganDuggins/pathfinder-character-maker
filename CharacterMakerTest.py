import unittest
import CharacterMaker

suite = unittest.TestLoader().loadTestsFromModule(test_me)
unittest.TextTestRunner(verbosity=2).run(suite)

