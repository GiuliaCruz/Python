from math import pi
import sys

def circle(radius):
    return pi * float(radius) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""\
              It's necessary to inform the radius of the circle
              Syntax: circle_area <radius>""")
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print('Circle area:', area)
    