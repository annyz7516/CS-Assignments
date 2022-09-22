DO NOT REMOVE THIS PARAGRAPH  
STUDENT ID: 47390751  
STUDENT NAME: Yue Zhang  
[]: add an 'x' inside the square brackets to declare that you haven't seen any other person's code

# COMP6010 S1 2022, External Offering

## Assignment 3

## Worth 10%

## Due: 17:00:00 Sydney Time, 15th May

## Late submissions not accepted

Student grades are stored in a csv file. The structure is fixed, as,

1. First line is the header.
2. Second and subseqent lines contain student data.
3. Each record is of the format:

```
Student ID, Assignment 1 Mark, Assignment 2 Mark, Practical Exam Attempt 1 Mark, Practical Exam Attempt 2 Mark
```

The three functions you need to completed are:

1. `get_totals` (4 marks): Returns a list of student totals, in order of occurrence in the spreadsheet. Total of a student is calculated as the sum of their marks for all assignments and practical exam. For the practical exam, the best of the two attempts should be used.
2. `top_student_basic` (4 marks): Returns the ID of the student who has the highest total. In case of a tie, return the ID of the first student, in order of occurrence in the spreadsheet.
3. `top_student_intermediate` (2 marks): Returns a list containing IDs of all students, in order of occurrence in the spreadsheet, that have the (equal) highest total.

IMPORTANT: You should write other helper functions to help you solve the problems. That is delegate as much as you can. Write simple functions and then call them to build on top of them.

A sample function is provided that returns a list containing students' assignment 1 marks. 

You cannot use **any** built-in functions, such as `max` or `min` or `sum`.

Please note that more spreadsheets will be used to test your submissions. Those spreadsheets may have tens and hundreds of students. So make sure you do not hard-code to the spreadsheet provided.