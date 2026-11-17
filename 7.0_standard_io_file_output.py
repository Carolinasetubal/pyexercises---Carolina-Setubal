"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: User input for one entry.
# 2. Process: Collect the data and save it to a CSV file.
# 3. Out, file name and columns: A CSV file with the recorded information.
# 4. Why these columns, and what this file is for: name and age. These help organise the information about each person.


# Your code below
import csv
import os

filename = "student_data.csv"

def save_entry():
    name = input("Enter name: ")
    age = input("Enter age: ")

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(filename) == 0:
            writer.writerow(["name", "age"])

        writer.writerow([name, age])

for i in range(2):
    save_entry()

# Final Results:
# The program collects a name and age.
# It saves two entries each time it runs.
# The CSV file has one header line.
# Running it three times adds six entries.
# Existing data is not overwritten.
# Invalid input is not checked yet.
