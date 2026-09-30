"""Main program for the Student Grade System."""

from student_input import get_student_details
from grade_calculator import calculate_result
from report_card import show_report
from student_data import save_student


def main():
    name, roll_no, marks = get_student_details()
    total, percentage, sgpa, result = calculate_result(marks)

    show_report(name, roll_no, marks, total, percentage, sgpa, result)

    record = {
        "Name": name,
        "Roll Number": roll_no,
        "Mathematics": marks[0],
        "Physics": marks[1],
        "Chemistry": marks[2],
        "Programming": marks[3],
        "English": marks[4],
        "Total": total,
        "Percentage": round(percentage, 2),
        "SGPA": round(sgpa, 2),
        "Result": result
    }
    save_student(record)
    print("Student data saved successfully.")


if __name__ == "__main__":
    main()
