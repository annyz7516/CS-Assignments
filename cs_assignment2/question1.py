import unittest

def is_odd(n):
    '''
    Returns True if n is odd, False otherwise
    '''
    if n%2==1:
        return True
    else:
        return False

class Tester(unittest.TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd(1))
        self.assertFalse(is_odd(2))
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(4))
        self.assertTrue(is_odd(5))
        self.assertFalse(is_odd(6))
        self.assertTrue(is_odd(7))
        self.assertFalse(is_odd(8))
        self.assertTrue(is_odd(9))
        self.assertFalse(is_odd(10))
        self.assertTrue(is_odd(-1729))
        self.assertFalse(is_odd(-1728))
        self.assertFalse(is_odd(0))

if __name__ == '__main__':
    unittest.main()