"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's answer about continuing a marketing campaign.
# 2. Process: Use a while loop to keep asking until the user says yes or reaches 5 attempts.
# 3. Out: A message showing whether the campaign was confirmed and the number of attempts.
# 4. My stop condition, my attempt limit, my summary: Stop condition: yes. Maximum 5 attempts. The summary shows the result and attempts.


# Your code below

# Block 1: Set the maximum attempts
attempts = 0
max_attempts = 5
answer = ""

# Block 2: Ask the user until the condition is met
while answer != "yes" and attempts < max_attempts:
    answer = input("Do you want to continue the marketing campaign? (yes/no): ")
    answer = answer.strip().lower()
    attempts = attempts + 1

# Block 3: Display the final result
if answer == "yes":
    print("Marketing campaign confirmed.")
else:
    print("Maximum number of attempts reached.")

# Block 4: Display the summary
print("Total attempts:", attempts)


# Test result:
# The while loop repeated the question until the user answered yes.
# It also stopped after 5 attempts if the answer was not yes.
# The program accepted YES, yes and extra spaces.
# The final summary showed the result and number of attempts.