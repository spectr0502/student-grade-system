"""Input checks for student details and marks."""


def valid_marks(value):
    try:
        marks = float(value)
        return 0 <= marks <= 100
    except ValueError:
        return False


def valid_student_name(name):
    return bool(name.strip())


def valid_roll_number(roll_no):
    return bool(roll_no.strip())
