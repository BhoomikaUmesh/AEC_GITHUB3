def print_pattern(rows):
    for i in range(1, rows+1):
        print("*" * i)

# User input for the number of rows in the pattern
rows = int(input("Enter the number of rows for the pattern: "))
print_pattern(rows)
