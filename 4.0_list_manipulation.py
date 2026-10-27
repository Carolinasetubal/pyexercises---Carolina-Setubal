"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 monthly marketing budgets.
# 2. Process: The program displays the lis, selects one budget, sorts the list and calculates the average.
# 3. Out: The original list, one selected budget, the sorted list and the average budget. 
# 4. What my list is about, and what I computed from it: My list contains monthly marketing budgets for 8 campaigns.
# I calculated the average to understand how much is spent per campaign. 


# Your code below

#Block 1: Create a list of monthly marketing budgets
budgets =  [1200, 2500, 1800, 3000, 1500, 2200, 2800, 2000] 

#Block 2: Display the whole list
print("Monthly marketing budgets: ", budgets)

#Block 3: Display one item from the list
print("First campaign budget:", budgets[0])

#Block 4: Sort the list from the smallest to largest
sorted_budgets = sorted(budgets)
print("Sorted budgets: ", sorted_budgets)

#Block 5: Calculate the average budget
average = sum(budgets) / len(budgets)
print("Average marketing budget:", average)


#Test Results
# The program displayed all 8 budgets correctly.
# It selected the first budget and sorted the values from smallest to largest.
# The average budget was 2125.
# I checked the average of the first three budgets manually:
# (1200 + 2500 + 1800) / 3 = 1833.33
# Python gives the same result for these three values.
# The results were what I expected.