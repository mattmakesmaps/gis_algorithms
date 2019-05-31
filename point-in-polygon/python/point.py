"""
Point Class
"""

from math import sqrt
class Point():
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __getitem__(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
        return None

    def __len__(self):
        return 2
    """
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x==other.x and self.y==other.y
        return NotImplemented

    def __ne__(self, other):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def __gt__(self, other):
        raise NotImplementedError

    def __ge__(self, other):
        raise NotImplementedError

    def __le__(self, other):
        raise NotImplementedError
    """

    def __str__(self):
        if type(self.x) is int and type(self.y) is int:
            return "({0},{1})".format(self.x,self.y)
        else:
            return "({0:.1f}, {1:.1f})".format(self.x, self.y)
    
    def __repr__(self):
        if type(self.x) is int and type(self.y) is int:
            return "({0},{1})".format(self.x,self.y)
        else:
            return "({0:.1f}, {1:.1f})".format(self.x, self.y)
    
    def distance(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)