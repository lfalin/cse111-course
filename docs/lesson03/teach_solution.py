import random
import textwrap

# Open the quotes.txt file.
with open("quotes.txt", "rt") as infile:

    # Read all the quotes in the file into a list.
    quotes = infile.readlines()

# Below is alternative code that doesn't use a with block:
#
# infile = open("quotes.txt", "rt")
# quotes = infile.readlines()
# infile.close()
#
# Notice that this alternative code must include infile.close(). The
# with block code above doesn't include calling the close function
# because the with block automatically calls the close function when the
# block ends.

# Ask the user how many quotes she would like to see.
quant = int(input("How many quotes would you like? "))

# Print the quotes requested by the user.
for _ in range(quant):
    # This for loop uses the underscore character (_) as a
    # variable name. The underscore is the variable name that
    # many programmers use when writing a counting loop that
    # doesn't use the variable in the body of the loop.

    # Randomly choose one quote.
    quote = random.choice(quotes)

    # Wrap the words of the quote if it is a long quote.
    wrapped = textwrap.wrap(quote, 70)

    # Print a blank line.
    print()

    # Print the wrapped quote.
    for line in wrapped:
        print(line)
