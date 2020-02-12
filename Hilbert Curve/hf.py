import inspect, itertools, math
from vector import *

none_class = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

def map(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

def backwards_string(string):
    return string[::-1]

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
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
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

