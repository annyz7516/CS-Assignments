import unittest

def get_acceptances(rsvps):
    '''
    Assuming that rsvps maps an integer to a boolean value,
    Return a list containing, in order of occurrence, all the
    integers that are mapped to True
    '''
    None

class Tester(unittest.TestCase):
    def test_get_acceptances(self):
        d1 = {1:False, 2:True, 3:True, 4:False, 5:True}
        self.assertEqual(get_acceptances(d1), [2, 3, 5])

        d2 = {200:False, 201:False, 203:True, 204:False, 205:False}
        self.assertEqual(get_acceptances(d2), [203])

        d3 = {200001:False, 200002:False, 200003:False, 200004:False, 200005:False}
        self.assertEqual(get_acceptances(d3), [])

if __name__ == '__main__':
    unittest.main()