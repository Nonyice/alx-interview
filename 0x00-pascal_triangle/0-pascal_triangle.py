def print_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if triangle:
            # Calculate the remaining elements of the row
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    
    # Print Pascal's triangle
    for row in triangle:
        print(" ".join(str(num) for num in row))

# Test the function
n = int(input("Enter the number of rows: "))
print_pascal_triangle(n)

