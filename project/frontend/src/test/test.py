import unittest

from functions import is_name, is_letter

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

    def test_is_letter(self):
        self.assertTrue(is_letter("L"))
        self.assertTrue(is_letter("i"))
        self.assertTrue(is_letter("I"))
        self.assertTrue(is_letter("ö"))
        self.assertFalse(is_letter("aa"))
        self.assertFalse(is_letter("xxxx"))
        self.assertFalse(is_letter("3"))
        self.assertFalse(is_letter("345435"))
        self.assertFalse(is_letter("KUKKA"))