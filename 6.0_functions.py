"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers (num1 and num2).
# 2. Process: Add the two numbers together.
# 3. Out: The sum of the two numbers.
# 4. My function name, and why return rather than print: add_numbers because it clearly describes what the function does.


# Your code below

def add_numbers(num1, num2):
    sum_result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum_result)
    return sum_result

sum = add_numbers(10, 20)
print(sum)
 
# Final Results:
# The function receives two numbers and adds them.
# add_numbers(10, 20) returns 30.
# The function works correctly.
# It returns the result instead of only printing it.
