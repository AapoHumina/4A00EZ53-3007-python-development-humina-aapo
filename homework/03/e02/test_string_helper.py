import unittest

from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        # with assertEqual you can check if two values the same:
        self.assertEqual(is_name("Ville Virtanen"), True)
        # but if the function just returns True or False, it may be easier
        # to use assertTrue of assertFalse:
        self.assertTrue(is_name("Ville Virtanen"))
        self.assertTrue(is_name("Li Xi"))
        self.assertTrue(is_name("Reijo Pohjolainen"))
        self.assertTrue(is_name("Juha Pohjalainen"))
        self.assertTrue(is_name("Vallu Virtanen"))
        self.assertTrue(is_name("Hilla Hotakainen"))
        self.assertTrue(is_name("Kauno Hui"))
        self.assertTrue(is_name("Heikki Heikki"))
        self.assertFalse(is_name("ville"))
        self.assertFalse(is_name("kalle Hotakainen"))
        self.assertFalse(is_name("3Hilla 6Hotakainen"))
        self.assertFalse(is_name("ville-Kalle Kulmala"))
        self.assertFalse(is_name("Adolf hilter"))
        self.assertFalse(is_name("josif Stalin"))
        self.assertFalse(is_name("3463456 S3453453"))
        self.assertFalse(is_name("K33l Sl4y3r"))
        self.assertFalse(is_name("dfghdfghdsfghdsfh"))
        self.assertFalse(is_name("Hajoo paskaas"))
        self.assertFalse(is_name("K33l Sl4y3r 3000 haha"))