"""Run: python -m unittest -v"""
import contextlib
import io
import unittest
from unittest.mock import patch
from grade_manager import (validate_mark, calculate_average, letter_grade,
                           read_positive_integer, main)


class GradeTests(unittest.TestCase):
    def test_valid_marks(self):
        for value in (0, 100, 45.5, " 82.5 "):
            with self.subTest(value=value):
                self.assertEqual(validate_mark(value), float(value))

    def test_invalid_marks(self):
        for value in (-1, 101, "abc", "", "nan", "inf", "-inf", None, True):
            with self.subTest(value=value):
                self.assertRaises(ValueError, validate_mark, value)

    def test_average(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90)
        self.assertEqual(calculate_average([0, 100]), 50)
        self.assertEqual(calculate_average([75]), 75)
        self.assertAlmostEqual(calculate_average([72.5, 80, 91]), 81.1666666667)

    def test_empty_or_invalid_marks(self):
        self.assertRaises(ValueError, calculate_average, [])
        self.assertRaises(ValueError, calculate_average, [50, 101])

    def test_all_grade_boundaries(self):
        cases = [(0,"F"),(59.999,"F"),(60,"D"),(69.999,"D"),
                 (70,"C"),(79.999,"C"),(80,"B"),(89.999,"B"),
                 (90,"A"),(100,"A")]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(letter_grade(value), expected)

    def test_grade_uses_unrounded_average(self):
        average = calculate_average([89.99, 90])
        self.assertLess(average, 90)
        self.assertEqual(letter_grade(average), "B")

    def test_invalid_average(self):
        self.assertRaises(ValueError, letter_grade, float("nan"))

    def test_count_validation(self):
        with patch("builtins.input", side_effect=["0", "-1", "1.5", "abc", "2"]):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(read_positive_integer("Count: "), 2)

    def test_full_session_and_retries(self):
        entries = ["2", "3", "", "S1", "", "Ali", "abc", "-1", "101",
                   "nan", "80", "90", "100", "s1", "S2", "Sara", "60", "70", "80"]
        output = io.StringIO()
        with patch("builtins.input", side_effect=entries):
            with contextlib.redirect_stdout(output):
                main()
        text = output.getvalue()
        for expected in ("Average: 90.00", "Letter grade: A", "Average: 70.00",
                         "Letter grade: C", "Student ID already exists",
                         "This field cannot be empty"):
            self.assertIn(expected, text)


if __name__ == "__main__":
    unittest.main()
