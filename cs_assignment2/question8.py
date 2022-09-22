import unittest

def all_odd(my_list):
    '''
    Return True if all items of my_list are odd, False otherwise
    '''
    None

class Tester(unittest.TestCase):
    def test_all_odd(self):
        list1 = [1, 2, 3, 4, 5, -6, -7, -8, 9, 10]
        self.assertFalse(all_odd(list1))
        list2 = [-1, -2, 3, 4, 5, -6, -7, -8, -9, -10]
        self.assertFalse(all_odd(list2))
        list3 = [-1, 3, -3, 5, -5]
        self.assertTrue(all_odd(list3))

if __name__ == '__main__':
    unittest.main()