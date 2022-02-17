import unittest

from string_helper import is_name, list_to_str

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        self.assertEqual(is_name("Ville Virtanen", ignore_case = False), True)
        self.assertTrue(is_name("Ville Virtanen", ignore_case = False))
        self.assertTrue(is_name("Li Xi", ignore_case = True))
        self.assertTrue(is_name("Reijo Pohjolainen", ignore_case = False))
        self.assertTrue(is_name("Juha Pohjalainen", ignore_case = True))
        self.assertTrue(is_name("Vallu Virtanen", ignore_case = False))
        self.assertTrue(is_name("Hilla Hotakainen", ignore_case = True))
        self.assertTrue(is_name("Kauno Hui", ignore_case = True))
        self.assertTrue(is_name("Heikki Heikki", ignore_case = False))
        self.assertFalse(is_name("ville", ignore_case = False))
        self.assertFalse(is_name("kalle Hotakainen", ignore_case = False))
        self.assertFalse(is_name("3Hilla 6Hotakainen", ignore_case = True))
        self.assertTrue(is_name("ville Kulmala", ignore_case = True))
        self.assertTrue(is_name("Adolf hilter", ignore_case = True))
        self.assertTrue(is_name("josif Stalin", ignore_case = True))
        self.assertFalse(is_name("3463456 S3453453", ignore_case = True))
        self.assertFalse(is_name("K33l Sl4y3r", ignore_case = True))
        self.assertFalse(is_name("dfghdfghdsfghdsfh", ignore_case = True))
        self.assertFalse(is_name("Hajoo paskaas", ignore_case = False))
        self.assertFalse(is_name("K33l Sl4y3r 3000 haha", ignore_case = True))
        self.assertFalse(is_name("    Aapo    Humina   ", ignore_case = True))
        self.assertFalse(is_name("    Aapo    Humina   ", ignore_case = False))
        self.assertTrue(is_name("ville-kalle Kulmala", ignore_case = True))
        self.assertTrue(is_name("Ville-Kalle Kulmala", ignore_case = False))
        self.assertFalse(is_name("-ville Kulmala", ignore_case = True))
        self.assertFalse(is_name(" ville-Kulmala", ignore_case = True))
        self.assertFalse(is_name(" ville-Kulmala ", ignore_case = False))
        self.assertFalse(is_name(" ville-Kulmala", ignore_case = False))
        self.assertRaises(Exception, is_name, 334554, True)
        self.assertRaises(Exception, is_name, True, False)
        self.assertRaises(Exception, is_name, 2345.4536, False)
        self.assertRaises(Exception, is_name, "Pekka Kulmala", 2345)
        self.assertRaises(Exception, is_name, "Pekka Kulmala", "ssdfsdf")

    def test_list_to_str(self):
        test_list = """
Database:
1: kakka
2: kikka
3: kokko """.strip()
        self.assertEqual(list_to_str(["kakka", "kikka", "kokko"]), test_list)
        test_list = """
Database:
1: kakka """.strip()
        self.assertEqual(list_to_str(["kakka"]), test_list)
        test_list = """
Database:
1: kakka
2: kikka
3: kokko
4: kikke
5: kukko
6: kekko """.strip()
        self.assertEqual(list_to_str(["kakka", "kikka", "kokko", "kikke", "kukko", "kekko"]), test_list)
        self.assertEqual(list_to_str([]), """Empty List""")
        self.assertRaises(Exception, list_to_str, "sdfsdfsdfdsf")
        self.assertRaises(Exception, list_to_str, 23432432)
