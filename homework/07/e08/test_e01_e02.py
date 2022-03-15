import unittest

from string_helper import csv_to_list
from validation import is_name

class TestE01E02(unittest.TestCase):
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


    def test_csv_to_list(self):
        csv_string="""1,Ville,Virtanen
2,Jussi,Virtanen"""
        self.assertEqual(csv_to_list(csv_string), [["1", "Ville", "Virtanen"], ["2", "Jussi", "Virtanen"]])
        self.assertRaises(Exception, csv_to_list, 23423)
        self.assertRaises(Exception, csv_to_list, {"23423"})
        self.assertRaises(Exception, csv_to_list, "Ville,Virtanen")
        csv_string="""1,Ville,Virtanen
Jussi,Virtanen"""
        self.assertRaises(Exception, csv_to_list, csv_string)

