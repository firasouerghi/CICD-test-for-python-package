
import unittest
from mock import patch
from challenge.main import circle_area, square_area


class TestAreas(unittest.TestCase):
    def test_circle_area_none_argument_raises(self):
        with self.assertRaises(ValueError):
            circle_area(None)

    def test_circle_area_int_argument_raises(self):
        with self.assertRaises(ValueError):
            circle_area(1)

    @patch('numpy.pi', 2)
    def test_circle_area_float_argument_success(self):
        area = circle_area(1.0)
        self.assertEqual(area, 2)

    def test_square_area_none_argument_raises(self):
        with self.assertRaises(ValueError):
            square_area(None)

    def test_square_area_int_argument_raises(self):
        with self.assertRaises(ValueError):
            square_area(1)

    def test_square_area_float_argument_success(self):
        area = square_area(1.0)
        self.assertEqual(area, 1)
