import unittest

from main import calculate_sum, palauta_isoin

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(-4, 4), 0)
        self.assertEqual(calculate_sum(-2, -2), -4)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1, 2), 3)
        self.assertEqual(calculate_sum("hello", "hello"), "hellohello")
    def test_palauta_isoin(self):
        self.assertEqual(palauta_isoin(1,2,3), 3)
        self.assertEqual(palauta_isoin(-1,2,3), 3)
        self.assertEqual(palauta_isoin(-1,-2,-3), -1)
        self.assertEqual(palauta_isoin(-1,2,-3), 2)
        self.assertEqual(palauta_isoin(3,3,3), 3)
        self.assertEqual(palauta_isoin(2,2,3), 3)
        self.assertEqual(palauta_isoin(1,1,3), 3)
        