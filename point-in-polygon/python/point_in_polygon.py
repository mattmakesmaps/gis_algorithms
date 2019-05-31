"""
Listing 2.9: The winding number algorithm
"""
from point import Point

def is_left(p, p1, p2):
    """
    Tests if point P is to the left of a line segment between p1 and p2
    Output
    0 the point is on the line
    >0 p is to the left of the line
    <0 p is to the right of the line
    """
    return (p2.x - p1.x) * (p.y-p1.y) - (p.x-p1.x) * (p2.y-p1.y)

def pip_wn1(pgon, point):
    """
    Determines whether a point is in a polyogn using the winding number algorithm without
    trigonometic functions. From Graphics Gems IV (Haines, 1994).
    Input:
    pgon: a list of points as the verticies for a polygon.
    point: the point
    Output:
    Returns a boolean value of True or False and the number of times the half-line croses
    the polygon boundary.
    """

    wn = 0
    n = len(pgon)
    for i in range(n-1):
        if pgon[i].y <= point.y:
            if pgon[i+1].y > point.y:
                if is_left(point, pgon[i], pgon[i+1]) > 0:
                    wn += 1
        else:
            if pgon[i+1].y <= point.y:
                if is_left(point, pgon[i], pgon[i+1]) < 0:
                    wn -= 1
    return wn is not 0, wn

if __name__ == "__main__":
    pgon = [ [2,3], [7,4], [6,6], [4,2], [11,5], [5,11], [2,3] ]
    ppgon = [Point(p[0], p[1]) for p in pgon]
    point = Point(6,4)

    print(pip_wn1(ppgon, point))
