import unittest

def sum_digits(n):
    '''
    Return the sum of all digits of n
    You may assume that n >= 0
    '''
    None

class Tester(unittest.TestCase):
    def test_sum_digits(self):
        self.assertEqual(sum_digits(1234), 10)
        self.assertEqual(sum_digits(12345), 15)
        self.assertEqual(sum_digits(123456), 21)
        self.assertEqual(sum_digits(1234567), 28)
        self.assertEqual(sum_digits(1729), 19)
        self.assertEqual(sum_digits(0), 0)

if __name__ == '__main__':
    unittest.main()