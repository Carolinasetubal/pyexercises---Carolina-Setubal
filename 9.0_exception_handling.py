"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: In: A number entered by the user.
# 2. Process: Convert the input into a number and divide 100 by it, handling errors.
# 3. Out: The result of the division or an error message.
# 4. The two failures, and whether they deserve the same message: Two failures: The user enters zero or text instead of a number. Both should produce different messages.

# Your code below

while True:
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        result = 100 / number
        print("Result:", result)
        break

    except ValueError:
        print("Invalid input. Please enter a number.")

    except ZeroDivisionError:
        print("You cannot divide by zero.")

# Final Results:
# A normal number gives the correct division result.
# Zero produces a division by zero error message.
# Text produces an invalid input error message.
# Empty input also produces an invalid input message.
# The program keeps running after invalid inputs.
# The two errors have different messages.
# Catching errors separately makes the messages clearer.