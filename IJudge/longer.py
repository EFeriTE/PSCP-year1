"""longer"""
import math
def long():
    """longee"""
    r,a,b = float(input()),float(input()),float(input())
    circle = 2 * math.pi * r
    rectangle = (a + b) * 2
    if circle > rectangle:
        print("Circle is longer")
    elif rectangle == circle:
        print("Equal")
    else:
        print("Rectangle is longer")
    mary = abs(circle - rectangle)
    print(f"{mary:.5f}")
long()
