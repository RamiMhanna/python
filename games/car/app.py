command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start" and not started:
        print("Car started...")
        started = True
    elif command == "start" and started:
        print("Car is already started .... type stop to stop it.")
    elif command == "stop" and started:
        print("Car stopped ....")
        started = False
    elif command == "stop" and not started:
        print("Car is already stopped .... type start to start it.")
    elif command == "help":
        print("""
start - to start the car 
stop - to stop the car 
quit - to quit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that ...")