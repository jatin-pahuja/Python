class Circle():
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

my_circle = Circle()           #here add your radius
print(my_circle.area())
