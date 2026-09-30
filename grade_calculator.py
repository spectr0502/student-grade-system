"""Functions for calculating grades and the student result."""


def get_grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    else:
        return 0


def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)

    grade_points = [get_grade_point(mark) for mark in marks]
    sgpa = sum(grade_points) / len(grade_points)

    if any(mark < 40 for mark in marks):
        result = "FAIL"
    else:
        result = "PASS"

    return total, percentage, sgpa, result
