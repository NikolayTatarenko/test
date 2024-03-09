import math

from point import Point

class Circle(Point):

    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x,y)
        self.radius = radius


    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def __add__(self, other):
        new_obj = super().__add__(other)
        return Circle(new_obj.x, new_obj.y, self.radius + other.radius)


    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y

        if self.radius == other.radius:
            return Point(new_x, new_y)
        else:
            new_radius = abs(self.radius - other.radius)
            return Circle(new_x, new_y, new_radius)


r_1 = Circle(0, 0, 3)
r_2 = Circle(0, 0, 2)
result = r_1 - r_2
print(result)