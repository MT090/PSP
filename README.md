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
- **Project_Report.docx**: Full PSP assignment report with requirements, design, testing, and tracking tables (complete tables before submission using `COPY_PASTE_DATA.txt`).
- **grade_manager.py**: Complete console program with seven functions.
- **test_grade_manager.py**: Nine test methods, including a full two-student session.
- **test_results.txt**: Captured successful test output.
- **TABLE_DATA_TO_FILL.txt**: Example data for filling report tables.
- **FILLING_INSTRUCTIONS.md**: Detailed step-by-step guide for completing tables.
- **COPY_PASTE_DATA.txt**: Quick copy-paste values for Word tables.

## Assumptions to confirm
The slide specifies neither language nor grade boundaries. This project uses
Python, equally weighted marks, and A >= 90, B >= 80, C >= 70, D >= 60,
otherwise F. Confirm these choices with the instructor. Grades use the
unrounded average; displayed averages have two decimal places.

## Project Tracking Data
The report (`Project_Report.docx`) includes PSP tracking tables that must be completed:
- **Job Number Log (Table 4)**: Record estimated and actual times for P01–P05.
- **Cumulative To Date Data (Table 5)**: Combine prior historical data with current project metrics.
- **Daily Time Log (Table 6)**: Log all work sessions with start/stop times and breaks.
- **Previous Work Job Number Log (Table 7)**: Historical assignments from earlier coursework.

See `TABLE_DATA_TO_FILL.txt` for example data and instructions.

Current project deliverables:
- 7 requirements (user input validation, calculations, display)
- 1 design document
- 7 functions in grade_manager.py
- 9 test methods in test_grade_manager.py
- 2 documentation files (README.md and Project_Report.docx)
