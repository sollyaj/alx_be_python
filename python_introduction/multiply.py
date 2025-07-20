rows = 5
i = 1  # row counter

while i <= rows:
    # Print spaces
    spaces = rows - i
    j = 1
    while j <= spaces:
        print(" ", end="")
        j += 1

    # Print asterisks
    stars = 2 * i - 1
    k = 1
    while k <= stars:
        print("*", end="")
        k += 1

    # Go to the next line
    print()
    i += 1
