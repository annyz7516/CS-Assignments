import unittest

def contains_multiple_of(my_list, n):
    '''
    Return True if my_list contains any multiple of n, False otherwise
    '''
    None

class Tester(unittest.TestCase):
    def test_contains_multiple_of(self):
        list1 = [1, 2, 4, 5, 6, 8, 9, 10]
        self.assertFalse(contains_multiple_of(list1, 15))
        self.assertFalse(contains_multiple_of(list1, 7))
        self.assertTrue(contains_multiple_of(list1, 8))
        self.assertTrue(contains_multiple_of(list1, 3))
        list2 = [240]
        self.assertFalse(contains_multiple_of(list2, 31))
        self.assertTrue(contains_multiple_of(list2, 120))
        list3 = [0]
        self.assertTrue(contains_multiple_of(list3, 15))
        self.assertTrue(contains_multiple_of(list3, 31))
        self.assertTrue(contains_multiple_of(list3, 15))

if __name__ == '__main__':
    unittest.main()