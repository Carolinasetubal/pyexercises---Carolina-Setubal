"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters two numbers.
# 2. Process: the program performs four mathematical operations.
# 3. Out: The results of addition, subtraction, multiplication and division.
# 4. What happens when the second number is zero, and why: if the second number is zero, the program displays a message because division by zero is not possible.



# Your code below
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# Sum of two numbers
sum = number_1 + number_2
print("The sum of the two numbers is: ", sum)

# Difference between the two numbers
diff = number_2 - number_1
print("The difference between the numbers is: ", diff)

# Multiplication of two numbers
product = number_1 * number_2
print("The product of the two numbers is: ", product)

# Division of two numbers
if number_2 != 0:
    division = number_1 / number_2
    print("The division of the two numbers is: ", division)
else:
    print("Cannot divide by zero.")


# Test Results
# 7 divided by 2 gives 3.5 when using /. If we use //, the result is 3.0 because it performs floor division. 
# When the second number is zero, the program displays a message instead of dividing.
