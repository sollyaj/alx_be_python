# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop for rows using while
while row < size:
    # Inner loop for columns using for
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
