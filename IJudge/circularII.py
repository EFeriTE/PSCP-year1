"""Circular II"""
import math
def circle():
    """Circular II"""
    x_mine = float(input())
    y_mine = float(input())
    r_mine = float(input())
    x_friend = float(input())
    y_friend = float(input())
    r_friend = float(input())
    d = math.sqrt(((x_mine-x_friend)**2)+((y_mine-y_friend))**2)
    sum_r = r_mine + r_friend
    if d < sum_r:
        print("Yes")
    else:
        print("No")
circle()
