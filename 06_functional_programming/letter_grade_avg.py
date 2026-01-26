'''
Docstring for 06_functional_programming.letter_grade_avg

Handles user i/o using functions from 06_functional_programming.grade_compute

    :expected input: 4 strings (A, A-, B+, B, ...) delimited by '$ '
        Ex. "A$ B+$ c$ a-"

    :expected output: ASCII Box (40x7) listing grades entered, lowest grade dropped,
        calculated average grade, and final letter grade
        Ex.'----------------------------------------
            |         GRADE REPORT SUMMARY         |
            ----------------------------------------
            | Grades Entered: A, B+, C, A-         |
            | Lowest Grade Dropped: C             |
            | Calculated Average:   3.7            |
            | Final Letter Grade:   A-             |
            ----------------------------------------
'''

import grade_compute as gc

# Use infinite loop because input_verify() detects user input of "Q" and uses the inbuilt method quit() to terminate
while True:
    grades_letter = gc.input_verify()
    grades_gpa = gc.gpa_parse(grades_letter)

    gc.print_summary(grades_letter, grades_gpa)