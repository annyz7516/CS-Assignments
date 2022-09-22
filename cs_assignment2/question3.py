import unittest

def sum(a, b):
    '''
    Return the sum of all integers from a to b
    (including both a and b)
    You may assume that a <= b
    '''
    None


class Tester(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(1, 3), 6)
        self.assertEqual(sum(1, 4), 10)
        self.assertEqual(sum(6, 15), 105)

if __name__ == '__main__':
    unittest.main()