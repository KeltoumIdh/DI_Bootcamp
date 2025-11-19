#Daily challenge
import math

def validate_circle_init(func):
    def wrapper(self, radius=None, diameter=None):
        if radius is None and diameter is None:
            raise ValueError("You must provide either a radius or a diameter.")
        if radius is not None and diameter is not None:
            raise ValueError("Provide only one: radius OR diameter, not both.")
        return func(self, radius, diameter)
    return wrapper

class Circle:
    @validate_circle_init
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        else:
            self.radius = diameter / 2

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius {self.radius} and diameter {self.diameter}"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("Can only add Circle to Circle")

    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius

    def __gt__(self, other):
        return isinstance(other, Circle) and self.radius > other.radius

    def __lt__(self, other):
        return isinstance(other, Circle) and self.radius < other.radius


c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=7)

print(c1)               # Circle with radius 5 and diameter 10
print(c2.area())        # 78.53981633974483
print(c1 + c3)          # Circle(radius=12)
print(c1 > c2)          # False
print(c1 == Circle(radius=5))  # True

circles = [c1, c2, c3]
print(sorted(circles))  # Sorted by radius