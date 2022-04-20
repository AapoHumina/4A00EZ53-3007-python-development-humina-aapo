import unittest

from functions import is_name

class Test(unittest.TestCase):
    def test_is_name(self):
        self.assertTrue(is_name("Ville"))
        self.assertTrue(is_name("Li"))
        self.assertTrue(is_name("Margareetta"))
        self.assertTrue(is_name("Kai"))
        self.assertTrue(is_name("Konstantin"))
        self.assertFalse(is_name("333333"))
        self.assertFalse(is_name("a"))
        self.assertFalse(is_name("23"))
        self.assertFalse(is_name("       @       "))
        self.assertFalse(is_name("L33T"))