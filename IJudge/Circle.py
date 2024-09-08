"""MathCal"""
import math

def circle_cal():
    """main"""
    radius = float(input())
    pie = math.pi
    circle_area(radius,pie)
    circle_aroud(pie,radius)

def circle_area(radius,pie):
    """area"""
    area = pie * radius**2
    print(f"Area: {area:.3f}")

def circle_aroud(pie, radius):
    """around"""
    around = 2 * pie * radius
    print(f"Circumference: {around:.3f}")

circle_cal()
