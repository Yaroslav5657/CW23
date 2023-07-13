from math_lib import pover, root

import unittest

class MathLibTestCase(unittest.TestCase):
    def testPover(self): 
        self.assertEqual(pover(0, 2), 0)
        self.assertEqual(pover(2, 0), 1)
        self.assertEqual(pover(-2, 0), 1)
        self.assertEqual(pover(2, -2), 0.25)

    def testRoot(self):
        self.assertEqual(root(10, 1), 10)
        self.assertEqual(root(10, 2), 3.1622776601683795)


if __name__ == '__main__':
    unittest.main()