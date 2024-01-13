import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        xy = (self.x, self.y)
        return hash(xy)
    
    def __str__(self):
        return f"Point({self.x, self.y})"    
    