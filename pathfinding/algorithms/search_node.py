from typing import Union
from point import Point

class Node(Point):
    def __init__(self, 
                 x: int, y: int, 
                 g: Union[float, int] = 0, 
                 h: Union[float, int] = 0, 
                 f: Union[float, int] = None, 
                 parent: 'Node' = None):
        super.__init__(x, y)
        self.g = g
        self.h = h
        if f is None:
            self.f = self.g + h
        else:
            self.f = f        
        self.parent = parent

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        xy = self.x, self.y
        return hash(xy)

    def __lt__(self, other):
        return self.f < other.f
    
    def __str__(self) -> str:
        return f"SearchNode({self.x}, {self.y})"