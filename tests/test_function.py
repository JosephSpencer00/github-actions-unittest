import unittest
import numpy as np
from function import abs_minus 

class TestAbsMinus(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(abs_minus(5, 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(abs_minus(-5, -3), 2)

    def test_mixed_sign_numbers(self):
        self.assertEqual(abs_minus(-5, 3), 8)
    
    def test_with_arrays(self):
        np.testing.assert_array_equal(
            abs_minus(np.array([1, -2, 3]), np.array([4, -2, 0])),
            np.array([3, 0, 3])
        )

    def test_float_numbers(self):
        self.assertAlmostEqual(abs_minus(5.5, 2.2), 3.3, places=7)

    def test_complex_numbers(self):
        self.assertAlmostEqual(abs_minus(1 + 2j, 1), 2, places=7)

if __name__ == '__main__':
    unittest.main()
