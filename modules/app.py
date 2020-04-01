from converters import maax

numbers = []
n = 0
while n < 5:
    x = int(input("Enter the numbers > "))
    numbers.append(x)
    n += 1

print(f"The list is: {numbers}")
print(f"the max in the list is: {maax(numbers)}")