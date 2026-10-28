"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 monthly marketing budgets.
# 2. Process: The program reorders the list in four different ways.
# 3. Out: Four reordered lists and the original file.
# 4. My four orders, and which ones modify the original: My four orders are original, reversed, ascending and descending.
# I use copies to avoid changing the original list.
# reverse() and sort() modify a list in place.
# reversed() and sorted() do not modify the original.


# Your code below
# Block 1: Create the original list
budgets = [1200, 2500, 1800, 3000, 1500, 2200, 2800, 2000]

# Block 2: Display the original order
print("Original budgets:", budgets)

# Block 3: Reverse the list using a copy
reversed_budgets = budgets.copy()
reversed_budgets.reverse()
print("Reversed budgets:", reversed_budgets)

# Block 4: Sort the list from smallest to largest
ascending_budgets = sorted(budgets)
print("Ascending budgets:", ascending_budgets)

# Block 5: Sort the list from largest to smallest
descending_budgets = budgets.copy()
descending_budgets.sort(reverse=True)
print("Descending budgets:", descending_budgets)

# Block 6: Check that the original list has not changed
print("Original list at the end:", budgets)

# Test results:
# The program displayed the budgets in four different orders.
# The original list remained unchanged.
# I used copies before applying reverse() and sort().
# The final list is identical to the one from Exercise 4.0.
# The results were what I expected.