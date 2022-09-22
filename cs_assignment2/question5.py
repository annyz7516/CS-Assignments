import unittest

def count_even_digits(n):
    '''
    Return the number of even digits of n.
    Note 0 by itself has no digits (not even, not odd)
    You may assume that n >= 0
    '''
    None

class Tester(unittest.TestCase):
    def test_count_even_digits(self):
        self.assertEqual(count_even_digits(12345), 2)
        self.assertEqual(count_even_digits(13579), 0)
        self.assertEqual(count_even_digits(0), 0)
        self.assertEqual(count_even_digits(-1729), 1)
        self.assertEqual(count_even_digits(1729), 1)
        self.assertEqual(count_even_digits(2468024680), 10)

if __name__ == '__main__':
    unittest.main()