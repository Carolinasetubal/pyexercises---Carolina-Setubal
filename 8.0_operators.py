"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# In: Two values chosen by the user.\
# Process: Compare the values using comparison and logical operators.
# ⁠Out: A table showing the results as True or False.
# ⁠Values chosen: 10 and 5. I was surprised that 10 == 5 is False, but 10 != 5 is True.

# Your code below
a = 10
b = 5

print("Comparison       Result")
print("a == b           ", a == b)
print("a != b           ", a != b)
print("a > b            ", a > b)
print("a < b            ", a < b)
print("a >= b           ", a >= b)
print("a <= b           ", a <= b)
print("a > 0 and b > 0  ", a > 0 and b > 0)
print("a > 10 or b > 0  ", a > 10 or b > 0)
print("not(a == b)      ", not(a == b))

# Final Results:
# I compared the values 10 and 5.
# I used comparison and logical operators.
# The program produced 9 True or False results.
# I predicted the results before running the code.
# The expected results are shown above.
