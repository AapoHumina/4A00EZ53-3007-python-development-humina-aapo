import unittest

from main import get_first_index

class TestMain(unittest.TestCase):
    def test_get_first_index(self):
        self.assertEqual(get_first_index("aapo", "a"), 0)
        self.assertEqual(get_first_index("kalle", "l"), 2)
        self.assertEqual(get_first_index("aapo", "o"), 3)
        self.assertEqual(get_first_index("aapo", "p"), 2)
        self.assertEqual(get_first_index("kaapo", "a"), 1)
        self.assertEqual(get_first_index("aapo", "x"), -1)
        self.assertEqual(get_first_index("kaaponen", "e"), 6)
        self.assertEqual(get_first_index("aapo", "f"), -1)
        self.assertEqual(get_first_index("m3m3", "3"), 1)
        self.assertEqual(get_first_index("0123456", "6"), 6)