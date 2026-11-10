
import math

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("Point:", (self.x, self.y))

    def distance(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        return d


# Creating two point objects

p1 = Point2D(2, 3)
p2 = Point2D(5, 7)

# Displaying points

p1.display()
p2.display()

# Calculating distance

print("Distance between points:", p1.distance(p2))
