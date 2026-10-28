"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a marketing cmampaign.
# 2. Process: Create a dictionary, read a field, change a value, remove a field and display the results.
# 3. Out: The campaign information and the updated dictionary.
# 4. My object, my five fields, and why those: My object is a marketing campaign. My five fields are name, brand, budget, platform and target audience. 
# These fields help me organize and manage a marketing campaign. 


# Your code below

# Block 1: Create a dictionary
campaign ={
    "name": "Summer Campaign",
    "brand": "Dior",
    "budget": 2500,
    "platform": "Instagram",
    "target_audience": "Young adults"
}

# Block 2: Display the dictionary
print("Original campaign:", campaign)

# Block 3: Read one field
print("Campaign name:", campaign["name"])

# Block 4: Change the budget
campaign["budget"] = 3000
print("Updated budget:", campaign["budget"])

# Block 5: Remove one field
campaign.pop("platform")
print("Campaign after removing platform:", campaign)

# Block 6: Display every field and its value
for key, value in campaign.items():
    print(key, ":", value)

# Block 7: Ask for a field
field = input("Enter a field to check: ")

if field in campaign:
    print("Field value:", campaign[field])
else:
    print("This field does not exist.")


 # Test Results
 #The program created a dictionary with five fields.
 #I changed the budget and removed the platform.
 #I displayed all the remaining fields and their values.
 #When I entered a field that did not exist, the program displayed a message instead of an error.
 #The results were what I expected.
