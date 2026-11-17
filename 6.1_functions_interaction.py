"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers.
# 2. Process, function by function: One function adds the numbers, another doubles the result, and the third checks if it is greater than 20.
# 3. Out: The final result and whether it is greater than 20.
# 4. The question my fourth function answers: It checks if the result is greater than 20. Splitting it into three sections makes the code easier to understand and test.


# Your code below
def add_numbers(a, b):
    return a + b

def double_number(number):
    return number * 2

def check_result(number):
    return number > 20


# Test each function
print(add_numbers(5, 3))
print(double_number(8))
print(check_result(16))

# Combine the functions
result = add_numbers(5, 10)
result = double_number(result)
print(check_result(result))

# Final Results
# Test 1: add_numbers(5, 3) returns 8
# Test 2: double_number(8) returns 16
# Test 3: check_result(16) returns False
# Combined result: True
# All functions work correctly.