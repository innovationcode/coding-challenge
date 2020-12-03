import unittest

from  Solution import get_days_of_power

class TestSum(unittest.TestCase):
      def test_1(self): 
            self.assertEqual(get_days_of_power(3000, 3, 500, 10, 1500, 7, 700000), 141) 
            self.assertEqual(get_days_of_power(500, 3, 500, 10, 500, 7, 21000), 17)
            self.assertEqual(get_days_of_power(1300, 0, 500, 0, 1500, 7, 10000), 5)
            self.assertEqual(get_days_of_power(10000, 3, 500, 10, 1500, 7, 11000), 1)

            self.assertEqual(get_days_of_power(1000, 2, 1000, 6, 1000, 6, 3000), 3)
            self.assertEqual(get_days_of_power(1000, 2 , 1000, 6, 1000, 6, 2999), 2)
            self.assertEqual(get_days_of_power(1000, 2, 1000, 6, 1000, 6, 0), 0)  
            self.assertEqual(get_days_of_power(0, 0, 0, 0, 0, 0, 2000), 0)
            self.assertEqual(get_days_of_power(1000, 0, 1000, 0, 1000, 0, 5000), 1)
            self.assertEqual(get_days_of_power(-1000, 2, 1000, 6, 1000, 6, 3000), -1)
            self.assertEqual(get_days_of_power(1000, -2, 1000, 6, 1000, 6, 3000), -1)


if __name__ == '__main__':
    unittest.main()