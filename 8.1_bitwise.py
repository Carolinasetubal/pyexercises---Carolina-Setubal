"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# ⁠In: A set of permissions represented by numbers.
# ⁠Process: Use bitwise operators to combine permissions, check if a permission exists, and remove one.
# ⁠Out: The permission values after each operation.
# ⁠Permissions: View, Edit and Publish. They represent what a user is allowed to do.

# Your code below
# Permissions
VIEW = 1
EDIT = 2
PUBLISH = 4

# Combine permissions
permissions = VIEW | EDIT
print("Combined:", bin(permissions))

# Check if Publish is present
print("Can publish:", bool(permissions & PUBLISH))

# Add Publish
permissions = permissions | PUBLISH
print("After adding Publish:", bin(permissions))

# Remove Edit
permissions = permissions & ~EDIT
print("After removing Edit:", bin(permissions))

# Final Results:
# VIEW = 001, EDIT = 010, PUBLISH = 100
# Combining VIEW and EDIT gives 011.
# PUBLISH is initially not present.
# Adding PUBLISH gives 111.
# Removing EDIT gives 101.
# The remaining permissions are VIEW and PUBLISH.

