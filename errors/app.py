try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
# Handling Division By Zero Error.
except ZeroDivisionError:
    print("Age can not be 0")
# Handling Invalid Input Error.
except ValueError:
    print("Invalid Value")
