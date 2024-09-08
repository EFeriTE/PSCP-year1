"""mosqito"""
from math import sqrt
def circular():
    """radius"""
    manx, many = float(input()), float(input())
    radius = float(input())
    mosx, mosy = float(input()), float(input())
    distant = sqrt(((mosx-manx)**2)+((mosy-many)**2))

    if distant <= radius:
        print("Yes")
    else:
        print("No")
circular()
