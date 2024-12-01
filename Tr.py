# Number of rows in the triangle
rows = 3

# Loop through each row
for i in range(1, rows + 1):
    # Print `i` stars for the current row
    print('*' * i)


# Initialize x and y with different values
x = 0
y = 5

# Loop until x is equal to y
while x != y:
    print(f"x = {x}, y = {y}")
    # Increment x to move it closer to y (to avoid an infinite loop)
    x += 1

print("Loop finished: x is now equal to y!")


