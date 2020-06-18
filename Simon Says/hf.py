import inspect, itertools, math, random
import numpy as np
from vector import *

none_class = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

def nf(i, n):
    return str(i).zfill(n)

def collision_rect_circle(rleft, rtop, width, height,   # rectangle definition
              center_x, center_y, radius):  # circle definition
    """ Detect collision between a rectangle and circle. """

    # complete boundbox of the rectangle
    rright, rbottom = rleft + width/2, rtop + height/2

    # bounding box of the circle
    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius

    # trivial reject if bounding boxes do not intersect
    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False  # no collision possible

    # check whether any point of rectangle is inside circle's radius
    for x in (rleft, rleft+width):
        for y in (rtop, rtop+height):
            # compare distance between circle's center point and each point of
            # the rectangle with the circle's radius
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True  # collision detected

    # check if center of circle is inside rectangle
    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True  # overlaid

    return False  # no collision detected

def circle_line_segment_intersection(circle_x, circle_y, circle_radius, x1, y1, x2, y2, full_line=True, tangent_tol=1e-9):
    """ Find the points at which a circle intersects a line-segment.  This can happen at 0, 1, or 2 points.

    :param circle_center: The (x, y) location of the circle center
    :param circle_radius: The radius of the circle
    :param pt1: The (x, y) location of the first point of the segment
    :param pt2: The (x, y) location of the second point of the segment
    :param full_line: True to find intersections along full line - not just in the segment.  False will just return intersections within the segment.
    :param tangent_tol: Numerical tolerance at which we decide the intersections are close enough to consider it a tangent
    :return Sequence[Tuple[float, float]]: A list of length 0, 1, or 2, where each element is a point at which the circle intercepts a line segment.

    Note: We follow: http://mathworld.wolfram.com/Circle-LineIntersection.html
    """

    circle_center = (circle_x, circle_y)
    pt1 = (x1, y1)
    pt2 = (x2, y2)

    (p1x, p1y), (p2x, p2y), (cx, cy) = pt1, pt2, circle_center
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx ** 2 + dy ** 2)**.5
    big_d = x1 * y2 - x2 * y1
    discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2

    if discriminant < 0:  # No intersection between circle and line
        return []
    else:  # There may be 0, 1, or 2 intersections with the segment
        intersections = [
            (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
             cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]  # This makes sure the order along the segment is correct
        if not full_line:  # If only considering the segment, filter out intersections that do not fall within the segment
            fraction_along_segment = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
            intersections = [pt for pt, frac in zip(intersections, fraction_along_segment) if 0 <= frac <= 1]
        if len(intersections) == 2 and abs(discriminant) <= tangent_tol:  # If line is tangent to circle, return just one point (as both intersections have same location)
            return [intersections[0]]
        else:
            return intersections

def vectorFromAngleFromPosition(x1, y1, x2, y2):
    return createVector(x1 - x2, y1 - y2)

def map(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

def backwards_string(string):
    return string[::-1]

def angleFromTwoPoints(x1, y1, x2, y2):
    myradians = math.atan2(y2 - y1, x2 - x1)
    mydegrees = math.degrees(myradians)

    return mydegrees

def in_circle(center_x, center_y, radius, x, y):
    square_dist = (center_x - x) ** 2 + (center_y - y) ** 2
    return square_dist <= radius ** 2

def positive(integer):
    return integer > 0

def lineFromAngleAndDistance(x1, y1, angle, length):
    x2 = x1 + math.cos(angle) * length
    y2 = x1 + math.cos(angle) * length

    return [x1, y1, x2, y2]


def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0:
        return createVector(0, 0)

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

    pt = createVector()
    pt.x = x1 + t * (x2 - x1)
    pt.y = y1 + t * (y2 - y1)

    return [pt, u]

def dist(*args):
    oneD = False
    twoD = False

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    if len(args) == 2:
        x1 = args[0]
        x1 = args[1]

        oneD = True

    if len(args) == 4:
        x2 = args[2]
        y2 = args[3]

        twoD = True
        oneD = False

    if twoD:
        dist = math.hypot(x2 - x1, y2 - y1)
    if oneD:
        dist = abs(x1 - y1)

    return dist



def printclass(t):
    if not inspect.isclass(t) and not isinstance(t, t.__class__):
        print("Pleas only pass classes to this function")
        return
    if t == object and not isinstance(t, t.__class__):
        return

    print(type(t).__name__, type(t))
    print(" ", "Methods: ")
    for func in dir(t):
        if callable(getattr(t, func)) and not func.startswith("__"):
            print(" ", " ", func, type(func))

    if len(t.__dict__.keys()) > 0:
        print("\n ", "Variables: ")
        for key in t.__dict__.keys():
            print(" ", " ", key + ": " + str(t.__dict__[key]), type(t.__dict__[key]))