import unittest

from string_helper import is_name
from string_helper import get_title

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        # with assertEqual you can check if two values the same:
        self.assertEqual(is_name("Ville Virtanen", ignore_case = False), True)
        # but if the function just returns True or False, it may be easier
        # to use assertTrue of assertFalse:
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



def test_get_title(self):
        
        test_title1 = """
------------------------------
-         Battleship         -
------------------------------
""".strip() # strip() will remove extra enters (\n} from start and end.

        self.assertEqual(get_title("battleship", 30, "-"), test_title1)

        test_title1 = """
xxxxxxxxxxxxxxxxxxxx
x       Aapo       x
xxxxxxxxxxxxxxxxxxxx
""".strip()

        self.assertEqual(get_title("aapo", 20, "x"), test_title1)

        test_title1 = """
--------------------
-    Battleship    -
--------------------
""".strip()

        self.assertEqual(get_title("battleship", 20, "-"), test_title1)
        self.assertEqual(get_title("leisure suit larry", 5, "h"), "invalid values, title length is > graph length")
        self.assertEqual(get_title("battletoad 2: revenge of the toadette", 10, "g"), "invalid values, title length is > graph length")