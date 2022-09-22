
import unittest

def occurences(data):
    """
    Given the list data, create a dictionary containing
    the number of occurences of every item in the list.
    """
    None

class Tester(unittest.TestCase):
    def test_occurences(self):
        self.assertEqual(occurences([10, 70, 20, 90]), {10:1, 70:1, 20:1, 90:1})
        self.assertEqual(occurences([10, 70, 20, 20, 20, 90, 70, 10]), {10:2, 70:2, 20:3, 90:1})
        
if __name__ == '__main__':
    unittest.main()