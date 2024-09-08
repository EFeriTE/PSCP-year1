"""math"""
import math
def main():
    """calculator"""
    x = (float(input()))
    y = (float(input()))
    r = abs(float(input()))
    xn = (float(input()))
    yn = (float(input()))
    d = (math.sqrt(((xn - x)**2) + ((yn - y)**2)))
    if d <= r:
        print("True")
    else:
        print("False")

main()
