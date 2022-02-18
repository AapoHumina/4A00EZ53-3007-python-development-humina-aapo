import unittest

from util.validation import is_date 

# The function checks if given date str is in ISO format: YYYY-MM-DD.  For example 2022-02-16.

class TestValidation(unittest.TestCase):
    def test_is_date(self):
        self.assertTrue(is_date("2022-10-10"))
        self.assertTrue(is_date("2000-01-01"))
        self.assertTrue(is_date("1993-10-10"))
        self.assertTrue(is_date("1111-10-30"))
        self.assertTrue(is_date("4500-12-24"))
        self.assertFalse(is_date("2022-33-33"))
        self.assertFalse(is_date("rghfghfghfh"))
        self.assertFalse(is_date("fghd-df-fg"))
        self.assertFalse(is_date("2022-00-00"))
        self.assertFalse(is_date({"2342", "3453", "34534"}))
        self.assertFalse(is_date(5436576457657))
        self.assertFalse(is_date(3453456.4567756))
        self.assertFalse(is_date(2335-12-12))
        self.assertFalse(is_date("kkkk-rr-ww"))
        self.assertFalse(is_date("DDDD-DD-DD"))
        self.assertFalse(is_date("0000-00-00"))
        self.assertFalse(is_date(("1234","12","12")))
        #self.assertRaises(Exception, is_date, 23423)
        #self.assertRaises(Exception, is_date, {"2342", "3453", "34534"})
        #self.assertRaises(Exception, is_date, 234.234)
        #self.assertRaises(Exception, is_date, 36457546865746845746857486548675)
        #self.assertRaises(Exception, is_date, "5656567567")

        