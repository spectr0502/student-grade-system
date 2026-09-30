import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from grade_calculator import get_grade_point, calculate_result


class GradeCalculatorTests(unittest.TestCase):
    def test_grade_points(self):
        self.assertEqual(get_grade_point(95), 10)
        self.assertEqual(get_grade_point(85), 9)
        self.assertEqual(get_grade_point(75), 8)
        self.assertEqual(get_grade_point(65), 7)
        self.assertEqual(get_grade_point(55), 6)
        self.assertEqual(get_grade_point(45), 5)
        self.assertEqual(get_grade_point(30), 0)

    def test_pass_result(self):
        total, percentage, sgpa, result = calculate_result([90, 80, 70, 60, 50])
        self.assertEqual(total, 350)
        self.assertEqual(percentage, 70)
        self.assertEqual(sgpa, 8)
        self.assertEqual(result, "PASS")

    def test_fail_result(self):
        self.assertEqual(calculate_result([90, 80, 70, 60, 39])[3], "FAIL")


if __name__ == "__main__":
    unittest.main()
