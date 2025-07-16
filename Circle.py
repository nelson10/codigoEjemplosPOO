class Circle:
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):
        return Circle.pi * self.radius ** 2

c1 = Circle(3)
c2 = Circle(5)
print(c1.area(), c2.area())  # Different values
