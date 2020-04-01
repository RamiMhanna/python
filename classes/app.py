class Animal:
    def walk(self):
        print("Walk")


class Dog(Animal):
    def bark(self):
        print("Bark")


class Cat(Animal):
    def be_annoying(self):
        print("Annoying")


cat_1 = Cat()
dog_1= Dog()
dog_1.walk()
dog_1.bark()
cat_1.be_annoying()
cat_1.walk()