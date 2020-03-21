secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guessed = int(input("Guess:"))
    guess_count += 1
    if guessed == secret_number:
        print("You Win !")
        break
# in python while loop has a else part which executed if the while loop finished without executing a break statement
else:
    print(f"your {guess_limit} tries is finished")

