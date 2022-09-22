import unittest

def count_negatives(my_list):
    '''
    Return the number of negative numbers in my_list
    '''
    None

class Tester(unittest.TestCase):
    def test_count_negatives(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(count_negatives(list1), 0)
        list2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        self.assertEqual(count_negatives(list2), 10)
        list3 = [-1, 2, -3, 0, -4]
        self.assertEqual(count_negatives(list3), 3)

if __name__ == '__main__':
    unittest.main()