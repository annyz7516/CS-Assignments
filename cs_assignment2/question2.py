import unittest

def higher_lower_equal(a, b):
    '''
    Returns a string that states whether a is higher, lower or equal to b
    if a is higher than b, return 'higher'
    if a is lower than b, return 'lower'
    if a is equal to b, return 'equal'
    '''
    if a > b:
        return 'higher'
    if a < b:
        return 'lower'
    if a == b:
        return 'equal'

class Tester(unittest.TestCase):
    def test_higher_lower_equal(self):
        self.assertEqual(higher_lower_equal(1, 2), 'lower')
        self.assertEqual(higher_lower_equal(2, 1), 'higher')
        self.assertEqual(higher_lower_equal(2, 2), 'equal')
        self.assertEqual(higher_lower_equal(1, 1), 'equal')
        self.assertEqual(higher_lower_equal(1, -1), 'higher')
        self.assertEqual(higher_lower_equal(-1, 1), 'lower')
        self.assertEqual(higher_lower_equal(-1, -1), 'equal')
        self.assertEqual(higher_lower_equal(0, 0), 'equal')
        self.assertEqual(higher_lower_equal(0, 1), 'lower')
        self.assertEqual(higher_lower_equal(1, 0), 'higher')
        self.assertEqual(higher_lower_equal(-1, 0), 'lower')
        self.assertEqual(higher_lower_equal(0, -1), 'higher')
        self.assertEqual(higher_lower_equal(0, -200), 'higher')  
        self.assertEqual(higher_lower_equal(-200, 0), 'lower')
        self.assertEqual(higher_lower_equal(200, 100), 'higher')
        self.assertEqual(higher_lower_equal(200, 200), 'equal')

if __name__ == '__main__':
    unittest.main()