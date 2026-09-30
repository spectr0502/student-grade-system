# Design and Documentation

## Objectives
Apply Python functions, modules, conditional statements, lists, calculations, validation, and CSV file handling in a grade-reporting application.

## Functional Requirements
1. Accept a student's name and roll number.
2. Accept marks for five named subjects.
3. Reject non-numeric marks and marks outside 0-100.
4. Calculate total marks and percentage.
5. Calculate grade points and SGPA using the documented scale.
6. Set PASS only if every subject mark is at least 40; otherwise set FAIL.
7. Display the report card.
8. Append the report to a CSV file.

## Non-Functional Requirements
- **Usability:** provide clear prompts and a readable report.
- **Reliability:** validate marks before calculations and use a consistent formula.
- **Maintainability:** separate input, validation, calculation, reporting, and storage.
- **Resource efficiency:** use the standard library and avoid unnecessary processing.
- **Portability:** support Python 3.8+ on common operating systems.

## System Architecture
```mermaid
flowchart TD
    A[User] --> B[main.py]
    B --> C[student_input.py]
    C --> D[validation.py]
    B --> E[grade_calculator.py]
    B --> F[report_card.py]
    B --> G[student_data.py]
    G --> H[(student_data.csv)]
```

## Process Workflow
```mermaid
flowchart TD
    A([Start]) --> B[Enter name and roll number]
    B --> C[Enter five subject marks]
    C --> D{All marks valid?}
    D -->|No| E[Show error and re-enter mark]
    E --> C
    D -->|Yes| F[Calculate total and percentage]
    F --> G[Calculate grade points and SGPA]
    G --> H{Every subject at least 40?}
    H -->|Yes| I[Set PASS]
    H -->|No| J[Set FAIL]
    I --> K[Display report card]
    J --> K
    K --> L[Save record to CSV]
    L --> M([End])
```

## Use Case Diagram
```mermaid
flowchart LR
    U((Student/User)) --> A[Enter student details]
    U --> B[Enter subject marks]
    U --> C[View report card]
    U --> D[Save report]
    A --> E[Student Grade System]
    B --> E
    C --> E
    D --> E
```

## Component Diagram
```mermaid
flowchart TB
    M[main.py] --> I[student_input.py]
    I --> V[validation.py]
    M --> C[grade_calculator.py]
    M --> R[report_card.py]
    M --> S[student_data.py]
    S --> F[(student_data.csv)]
```

## Sequence Diagram
```mermaid
sequenceDiagram
    actor User
    participant Main as main.py
    participant Input as student_input.py
    participant Calc as grade_calculator.py
    participant Report as report_card.py
    participant Store as student_data.py
    User->>Main: Run program
    Main->>Input: Request details and marks
    Input-->>Main: Return valid inputs
    Main->>Calc: Calculate summary
    Calc-->>Main: Total, percentage, SGPA, result
    Main->>Report: Display report card
    Report-->>User: Show result
    Main->>Store: Save student record
    Store-->>Main: Save complete
```

## Storage Design
The project uses a CSV file named `student_data.csv`. Each row contains name, roll number, five subject marks, total, percentage, SGPA, and result. New records are appended, so previous entries remain available.

## Design Decisions and Rationale
- The command-line interface keeps the project easy to run.
- Calculation logic is separated from input and display logic.
- CSV storage is simple and supported by the Python standard library.
- The grade-point scale is explicit and easy to test.
- SGPA is calculated as the average of five grade points; official institutions may use credit-weighted calculations.

## Testing Approach
Unit tests check grade-point boundaries, a passing case, and a failing case. Manual testing should include valid marks, invalid text, out-of-range marks, and confirming that the CSV file is created and appended.

## Challenges
Important considerations include validating user-entered marks, applying the same grade scale consistently, and saving all calculated values in a structured format.

## Learnings
The project practices modular Python design, functions, lists, conditional logic, input validation, arithmetic calculations, CSV handling, and unit testing.

## Future Enhancements
- Add student search and record editing
- Add a menu to view previous reports
- Support subject credits for institution-specific SGPA
- Export formatted report cards
- Add a graphical interface
