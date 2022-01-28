def calculate_sum(num1, num2):
    sum = num1 +num2
    return sum

sum = calculate_sum(4,4)
print(sum)


import unittest

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(-4, 4), 0)
        self.assertEqual(calculate_sum(-2, -2), -4)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1, 2), 3)
        self.assertEqual(calculate_sum("hello", "hello"), "hellohello")
        