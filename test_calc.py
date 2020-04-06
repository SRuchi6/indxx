import calc_percentile
import unittest

class TestCalc(unittest.TestCase):

    def test_percentile(self):
        marks = [80, 78, 90, 67, 86, 99, 54, 76, 89, 40]

        self.assertEqual(calc_percentile.percentile(marks,5),60.0)
        self.assertEqual(calc_percentile.percentile(marks,60), "Input value if greater than length of list")
        self.assertEqual(calc_percentile.percentile(marks,6),90.0)
        self.assertEqual(calc_percentile.percentile(marks,10),0.0)
        self.assertRaises(IndexError, calc_percentile.percentile, [], -1)


if __name__ == "__main__":
    unittest.main()