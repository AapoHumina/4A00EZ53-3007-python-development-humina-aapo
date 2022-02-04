def number_range(starting_number, ending_number, how_many_steps=1):
    returning_number = ""
    for number in range (starting_number,ending_number,how_many_steps ):
        returning_number=returning_number + str(number) + ","
    returning_number = returning_number + str(number + how_many_steps)
    return returning_number



print(number_range(1, 10, 1))
print(number_range(0, 10, 2))
print(number_range(10, 0, -1))
print(number_range(-10,0,1))

import unittest

class TestMain(unittest.TestCase):
    def test_number_range(self):
        self.assertEqual(number_range(3,8,1), "3,4,5,6,7,8")
        self.assertEqual(number_range(10,0,-1), "10,9,8,7,6,5,4,3,2,1,0")
        self.assertEqual(number_range(3,8), "3,4,5,6,7,8")
        self.assertEqual(number_range(7,10,3), "7,10")
        self.assertEqual(number_range(-10,0,1), "-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0")
        self.assertEqual(number_range(100,0,-10), "100,90,80,70,60,50,40,30,20,10,0")
        self.assertEqual(number_range(-10,-2,2), "-10,-8,-6,-4,-2")
        self.assertEqual(number_range(-10,-20,-2), "-10,-12,-14,-16,-18,-20")
