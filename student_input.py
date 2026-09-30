"""Collect student details and subject marks from the user."""

from validation import valid_marks, valid_roll_number, valid_student_name

SUBJECTS = ["Mathematics", "Physics", "Chemistry", "Programming", "English"]


def get_student_details():
    print("\\n===== STUDENT GRADE SYSTEM =====")

    while True:
        name = input("Enter student name: ").strip()
        if valid_student_name(name):
            break
        print("Name cannot be empty.")

    while True:
        roll_no = input("Enter roll number: ").strip()
        if valid_roll_number(roll_no):
            break
        print("Roll number cannot be empty.")

    marks = []
    print("\\nEnter marks out of 100")
    for subject in SUBJECTS:
        while True:
            value = input(subject + ": ").strip()
            if valid_marks(value):
                marks.append(float(value))
                break
            print("Enter a number between 0 and 100.")

    return name, roll_no, marks
