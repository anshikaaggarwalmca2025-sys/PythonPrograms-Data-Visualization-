#draw diamond pattern if number of rows and iteration are given by user and it must be positive and if the number is positive then print the pattern else dont print and it must have space in the left side

rows = int(input("Enter number of rows: "))
if rows <= 0:
    print("Invalid number of rows")
else:
    # Upper half (including middle row)
    for i in range(1, rows + 1):
        print(" " * (rows - 2*i + "* " * i)
    # Lower half
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - 2*i + "* " * i)