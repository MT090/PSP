# Student Grade Management System

## Run
Requires Python 3.10 or later. No extra packages are needed.
Extract the ZIP and open a terminal in the project folder:

```sh
python grade_manager.py
python -m unittest -v
```

On Windows, use `py` instead of `python` if needed.

Enter student and subject counts, then each student's ID, name, and marks.
The program rejects invalid input and asks again. Student IDs must be unique
(case-insensitive). Marks accept decimals from 0 to 100 inclusive.
All students use the same subject count. Results remain in memory for this session only.

## Files
- Project_Report.docx: requirements, design, testing, worked example, and logs.
- grade_manager.py: complete console program with seven functions.
- test_grade_manager.py: nine test methods, including a full two-student session.
- test_results.txt: captured successful test output.

## Assumptions to confirm
The slide specifies neither language nor grade boundaries. This project uses
Python, equally weighted marks, and A >= 90, B >= 80, C >= 70, D >= 60,
otherwise F. Confirm these choices with the instructor. Grades use the
unrounded average; displayed averages have two decimal places.

## Complete your records
Enter your name, ID, course, and section in the report.
Its estimates are proposed planning values, not a claim of prior estimates.
Record your estimates before doing each job yourself, and log real session
times and interruptions as you work. Sum each job's net minutes, transfer
them to the Job Number Log, and update cumulative data.

Previous assignments and your actual working times are blank because they
were not supplied. Add verified data from your existing Daily Time Log.
Leave historical estimates blank if unavailable. Do not treat the worked
examples as your personal records. Use official instructor forms if supplied;
the slide did not include them.

Actual unit counts refer to the supplied deliverables: seven requirements,
one design description, seven program functions, nine test methods, and
two documents (report and README). Keep cumulative units separate by type.
