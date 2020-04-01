class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, I am  {self.name}")


user_input = input("Enter your name please >")
person = Person(input)
person.talk()
