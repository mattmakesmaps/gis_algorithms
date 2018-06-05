"""
LISTING 2.4 of GIS Algorithms, Xiao.
"""
from point import Point

def centroid(pgon):
    """
    Calcualtes the centroid and area of a polygon.
    Input:
    pgon: a list of Point objects
    Output:
    A: the area of the polygon
    C: the centroid of the polygon
    """
    numvert = len(pgon)
    A = 0 # set area to zero
    xmean = 0
    ymean = 0

    # loop through all verts but for the last
    # duplicate closing vert.
    for i in range(numvert-1):
        # huh?
        ai = pgon[i].x * pgon[i+1].y - pgon[i+1].x * pgon[i].y
        A += ai
        xmean += (pgon[i+1].x + pgon[i].x) * ai
        ymean += (pgon[i+1].y + pgon[i].y) * ai
    A = A/2.0
    C = Point(xmean/ (6*A), ymean / (6*A))
    return A, C

# TEST
if __name__ == '__main__':
    points = [ 
        [0,10], [5,0], [10,10], [15,0], [20,10],
        [25,0], [30,20], [40,20], [45,0], [50,50],
        [40,40], [30,50], [25,20], [20,50], [15,10],
        [10,50], [8,8], [4,50], [0,10]
    ]

    polygon = [Point(p[0], p[1]) for p in points]

    print(centroid(polygon))