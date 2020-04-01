# Numbers
# Strings
# Booleans
# ---------
# Lists
# Dictionaries
# ---------
# Classes

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")
        print(f"{point_1.x}|{point_1.y}")


point_1 = Point()
point_1.x = 10
point_1.y = 20
point_1.draw()
