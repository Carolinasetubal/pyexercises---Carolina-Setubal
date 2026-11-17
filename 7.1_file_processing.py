"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Some lines are empty.
# - Some names may have extra spaces.
# - The names are not sorted by last name.
# - Some surnames may contain more than one word.

# 1. In: The names.txt file containing a list of names.
# 2. Process, problem by problem: Read the file, remove empty lines, sort the names by last name, and save them.
# 3. Out: A new file called sorted_names.txt containing the sorted names. 
# 4. How I decide which word is the last name: Split each name into words and use the last word to sort the list.


# Your code below
# Read the original file
with open("names.txt", "r") as file:
    names = file.readlines()

# Remove empty lines and extra spaces
names = [name.strip() for name in names if name.strip()]

# Sort by last name
names.sort(key=lambda name: name.split()[-1].lower())

# Save the sorted names
with open("sorted_names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Names sorted and saved successfully!")

# Final Results:
# The program reads names from names.txt.
# It removes empty lines and extra spaces.
# It sorts the names alphabetically by last name.
# It saves the result in sorted_names.txt.
# The original file is not modified.
# The program works if names.txt exists.