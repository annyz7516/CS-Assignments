
import unittest

def are_mutually_reverse(list1, list2):
    '''
    Return True if the two lists are mutually reverse, False otherwise
    You may not use any built in function besides
    len(list) and accessing attributes using index
    '''
    None

class Tester(unittest.TestCase):
    def test_are_mutually_reverse(self):
        list1 = [1, 2, 3]
        list2 = [3, 2, 1]
        self.assertTrue(are_mutually_reverse(list1, list2))
        list2 = [3, 2, 4]
        self.assertFalse(are_mutually_reverse(list1, list2))
        list2 = [4, 2, 1]
        self.assertFalse(are_mutually_reverse(list1, list2))
        list2 = [3, 2, 1, 0]
        self.assertFalse(are_mutually_reverse(list1, list2))
        list1 = [0]*1000
        list2 = [0]*1000
        list1[0] = 8
        list2[-1] = 8
        self.assertTrue(are_mutually_reverse(list1, list2))

if __name__ == '__main__':
    unittest.main()