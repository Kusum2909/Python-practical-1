
import math

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("2D Point:", (self.x, self.y))

    def distance(self, p):
        return math.sqrt(
            (p.x - self.x)**2 +
            (p.y - self.y)**2
        )


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print("3D Point:", (self.x, self.y, self.z))

    def distance(self, p):
        return math.sqrt(
            (p.x - self.x)**2 +
            (p.y - self.y)**2 +
            (p.z - self.z)**2
        )


# Creating two 3D point objects

p1 = Point3D(2, 3, 4)
p2 = Point3D(5, 7, 8)

# Display points

p1.display()
p2.display()

# Calculate distance

print("Distance between points:", p1.distance(p2))
