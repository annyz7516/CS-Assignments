
import unittest

class Box:
    def __init__(self, depth, height, width):
        '''
        Initialize the object with the 
        given depth, height, and width
        '''
        None
    
    def volume(self):
        '''
        Return volume calculated as the product
        of the three sides
        '''
        None

    def __eq__(self, other):
        '''
        HD Question (worth 2 marks)
        Return True if the calling objet and the parameter
        object are identical, after orienting them if needed
        For example, a 2 by 5 by 3 box is 
        identical to a 5 by 2 by 3 box.
        '''
        None

class Tester(unittest.TestCase):
    def test_init(self):
        a = Box(1, 2, 3)
        self.assertEqual(a.depth, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.width, 3)
        b = Box(4, 8, 3)
        self.assertEqual(b.depth, 4)
        self.assertEqual(b.height, 8)
        self.assertEqual(b.width, 3)
    
    def test_volume(self):
        a = Box(1, 2, 3)
        self.assertEqual(a.volume(), 6)
        b = Box(4, 8, 3)
        self.assertEqual(b.volume(), 96)

    def test_eq(self):
        a = Box(1, 2, 3)
        b = Box(2, 1, 3)
        self.assertTrue(a == b)
        b = Box(2, 1, 4)
        self.assertFalse(a == b)
        b = Box(3, 2, 1)
        self.assertTrue(a == b)
        b = Box(1, 2, 4)
        self.assertFalse(a == b)

if __name__ == '__main__':
    unittest.main()