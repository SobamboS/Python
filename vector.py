import math

class Vector:

 def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

 def __abs__(self):
    return math.hypot(self.x, self.y)

 def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)

 def __str__(self):
     return f"{self.x}i+{self.y}j"

 def __repr__(self):
    return f"Vector({self.x}i+{self.y}"

 def __len__(self):
     return 0

def __bool__(self):
    return True

def __lt__(self, other):
    return abs(self) < abs(other)


v1 = Vector(2, 4)
v2 = Vector(1, 6)
print(v1)
v3 = v1 + v2

lst = [v3, v1, v2]
print(lst)
lst.sort()
print(lst)