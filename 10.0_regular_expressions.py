"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# In: Three text values: a valid email, a phone number and a password.
# ⁠Process: Use regular expressions to check whether each value matches the required pattern.
# ⁠Out: A message showing whether each value is valid or invalid.
# ⁠Three rules: The email must have an @ and a domain, the phone number must have 9 digits, and the password must have at least 8 characters, including a letter and a number.
 
# Your code below
import re

def check_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))

def check_phone(phone):
    return bool(re.fullmatch(r"\d{9}", phone))

def check_password(password):
    return bool(re.fullmatch(r"(?=.[A-Za-z])(?=.\d).{8,}", password))


email = input("Enter an email: ")
phone = input("Enter a phone number: ")
password = input("Enter a password: ")

print("Email valid:", check_email(email))
print("Phone valid:", check_phone(phone))
print("Password valid:", check_password(password))

# Final Results:
# The email pattern checks the address format.
# The phone pattern requires exactly 9 digits.
# The password requires at least 8 characters,
# including a letter and a number.
# Valid inputs return True.
# Invalid inputs return False.
# The patterns check format, not whether the
# information is real or secure.
 
