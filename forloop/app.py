matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]
print(matrix)
x = matrix[0][2]
print(x)
print()
for row in matrix:
    for col in row:
        print(col)
print()
list_of_numbers = [4, 6, 2, 8, 1, 9, 3]
largest_number = 0
for num in list_of_numbers:
    if num > largest_number:
        largest_number = num
print(f"The largest number in the list is: {largest_number}")


