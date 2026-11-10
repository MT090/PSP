"""Student Grade Management System. Run with Python 3.10 or later."""
import math


def validate_mark(value):
    """Return a finite numeric mark in the inclusive range 0 to 100."""
    if isinstance(value, bool):
        raise ValueError("Enter a number from 0 to 100.")
    try:
        mark = float(value)
    except (ValueError, TypeError, OverflowError):
        raise ValueError("Enter a number from 0 to 100.") from None
    if not math.isfinite(mark) or not 0 <= mark <= 100:
        raise ValueError("Enter a number from 0 to 100.")
    return mark


def calculate_average(marks):
    values = [validate_mark(mark) for mark in marks]
    if not values:
        raise ValueError("At least one mark is required.")
    return math.fsum(values) / len(values)


def letter_grade(average):
    average = validate_mark(average)
    for threshold, grade in ((90, "A"), (80, "B"), (70, "C"), (60, "D")):
        if average >= threshold:
            return grade
    return "F"


def read_positive_integer(prompt):
    while True:
        text = input(prompt).strip()
        if text.isascii() and text.isdecimal() and int(text) > 0:
            return int(text)
        print("Enter a positive whole number.")


def read_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_mark(prompt):
    while True:
        try:
            return validate_mark(input(prompt))
        except ValueError as error:
            print(error)


def main():
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("Scale: A >= 90; B >= 80; C >= 70; D >= 60; F < 60")
    print("All subjects have equal weight. Press Ctrl+C to cancel.")
    count = read_positive_integer("Number of students: ")
    subject_count = read_positive_integer("Number of subjects per student: ")
    students = []
    used_ids = set()
    for index in range(count):
        print(f"\nStudent {index + 1}")
        while True:
            student_id = read_nonempty("Student ID: ")
            if student_id.casefold() not in used_ids:
                break
            print("Student ID already exists. Enter a different ID.")
        used_ids.add(student_id.casefold())
        name = read_nonempty("Student name: ")
        marks = [read_mark(f"Subject {i + 1} mark (0-100): ")
                 for i in range(subject_count)]
        average = calculate_average(marks)
        students.append((student_id, name, marks, average, letter_grade(average)))
    print("\nRESULTS")
    for student_id, name, marks, average, grade in students:
        print(f"\nID: {student_id}\nName: {name}")
        print("Marks: " + ", ".join(f"{mark:g}" for mark in marks))
        print(f"Average: {average:.2f}\nLetter grade: {grade}")
    print("\nResults are kept only for this session.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled. No complete result report was generated.")
