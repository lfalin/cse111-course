import csv

# Create an empty dictionary that will store student
# information with the I-Number number as the key.
students = {}

# Open a file named students.csv and store a reference
# to the opened file in a variable named infile.
with open("students.csv", "rt") as infile:

    # Use the csv module to create a reader
    # object that will read from the opened file.
    reader = csv.reader(infile)

    # The first line of the CSV file contains column headings
    # and not a student's I-Number and name, so this statement
    # skips the first line of the CSV file.
    next(reader)

    # Read each row in the CSV file one at a time as a list.
    for row in reader:

        # For the current row, retrieve
        # the values in columns 0 and 1.
        inumber = row[0]
        name = row[1]

        # Add a student's I-Number and name
        # to the students dictionary.
        students[inumber] = name


# Get an I-Number from the user.
inum = str(input("Please enter an I-Number (xx-xxx-xxxx): "))

# The I-Numbers are stored in the CSV file as digits only (without
# any dashes), so we remove all dashes from the user's input.
inum = inum.replace("-", "")

# Determine if the user input is formatted correctly.
if inum.isdigit():
    if len(inum) < 9:
        print("Invalid I-Number: too few digits")
    elif len(inum) > 9:
        print("Invalid I-Number: too many digits")
    else:
        # The user input is a valid I-Number. Find
        # the I-Number in the list of I-Numbers.
        if inum in students:
            # Retrieve the student name that corresponds
            # to the I-Number that the user entered.
            name = students[inum]

            # Print the student name.
            print(name)
        else:
            print("No such student")
else:
    print("Invalid character in I-Number")
