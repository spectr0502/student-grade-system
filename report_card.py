"""Display the student's report card."""


def show_report(name, roll_no, marks, total, percentage, sgpa, result):
    subjects = ["Mathematics", "Physics", "Chemistry", "Programming", "English"]

    print("\\n===== STUDENT REPORT CARD =====")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("\\nSubject-wise Marks:")

    for subject, mark in zip(subjects, marks):
        print(subject + ":", mark)

    print("\\nTotal Marks:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("SGPA:", round(sgpa, 2))
    print("Result:", result)
    print("================================")
