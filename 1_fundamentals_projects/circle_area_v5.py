from math import pi
import sys

def help():
    print("""\
              It's necessary to inform the radius of the circle
              Syntax: circle_area <radius>""")

def circle(radius):
    return pi * float(radius) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print('Circle area:', area)
    