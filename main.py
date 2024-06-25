# Define a two-dimensional array (3x3 matrix)
two_dimensional_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Initialize counters for rows and columns
counter_row = 0
counter_index = 0

# Loop through each row in the two-dimensional array
for rows in two_dimensional_array:
    # Loop through each element in the current row
    for index in rows:
        # Print the element at the current row and column position
        print(two_dimensional_array[counter_index][counter_row], end=" ")
        # Move to the next row in the same column
        counter_index += 1

    # Print a newline character after finishing one row
    print()
    # Reset counter_index to 0 to start from the first row in the next column
    counter_index = 0
    # Move to the next column
    counter_row += 1
