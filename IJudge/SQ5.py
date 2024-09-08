"""SQ"""
import math
def sq():
    """5"""
    num = int(input())
    row = math.ceil(num/7)
    ends = num - 7
    again = num
    for _ in range(row):
        if ends <= 0:
            ends = 0
        for i in range(again,ends,-1):
            print(i,end=" ")
        print()
        ends -= 7
        again -= 7

sq()
