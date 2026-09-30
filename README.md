# Student Grade System

**Student Name:** Abhishek Kumar  
**Registration Number:** 26BSA10029  
**Date:** 30 September 2026

## Overview
A command-line Student Grade System written in Python. It accepts a student's name, roll number, and marks in five subjects. It calculates total marks, percentage, SGPA, and PASS/FAIL status, displays a report card, and saves the record in a CSV file.

## Features
- Enter student name and roll number
- Enter marks for Mathematics, Physics, Chemistry, Programming, and English
- Validate marks from 0 to 100
- Calculate total marks and percentage
- Calculate SGPA using the project's grade-point scale
- Determine PASS/FAIL (all subjects must have at least 40 marks to pass)
- Display a report card
- Save records in `student_data.csv`

## Technologies
- Python 3.8 or above
- Python standard library (`csv`, `pathlib`, `unittest`)
- No external libraries required

## Project Structure
- `src/main.py` - starts the program and coordinates modules
- `src/student_input.py` - collects student details and marks
- `src/validation.py` - validates user input
- `src/grade_calculator.py` - calculates grade points, total, percentage, SGPA, and result
- `src/report_card.py` - displays the report card
- `src/student_data.py` - saves and reads CSV records
- `tests/test_grade_calculator.py` - automated calculation tests
- `docs/design.md` - requirements and diagrams
- `statement.md` - problem statement and project scope
- `project_report.pdf` - detailed report

## Grade Point Scale
| Marks | Grade Point |
|---|---:|
| 90-100 | 10 |
| 80-89.99 | 9 |
| 70-79.99 | 8 |
| 60-69.99 | 7 |
| 50-59.99 | 6 |
| 40-49.99 | 5 |
| Below 40 | 0 |

SGPA is the average of the five subject grade points. This is a simplified project calculation and may differ from an institution's official credit-weighted SGPA method.

## Install and Run
1. Extract the ZIP file.
2. Open the extracted folder in VS Code or a terminal.
3. Change to the source folder:
   ```bash
   cd src
   ```
4. Run:
   ```bash
   python main.py
   ```
   Use `python3 main.py` if that is the command for your system.
5. Enter the requested student details and marks.

The CSV file is created in the project root after the first record is saved.

## Testing
From the project root, run:
```bash
python -m unittest discover -s tests -v
```
Tests cover the grade-point scale, a passing result, and a failing result. Manually test marks at 0 and 100, invalid text, marks outside the range, and CSV record creation.

## Non-Functional Requirements
- **Usability:** clear prompts and a readable report card.
- **Reliability:** marks are checked before calculation.
- **Maintainability:** input, calculation, display, and storage are separated into modules.
- **Resource efficiency:** uses only the Python standard library and a small CSV file.
- **Portability:** runs on systems with Python 3.8 or above.

## Data Storage
Student data is appended to `student_data.csv`. Unlike an in-memory-only version, the CSV file remains available after the program exits.
