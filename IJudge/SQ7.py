"""Sq"""
def sq():
    """7"""
    num = int(input())
    for j in range(num):
        for i in range(1,j+2):
            print(i,end=" ")
        print()
    for l in range(num,1,-1):
        for k in range(1,l):
            print(k,end=" ")
        print()
sq()
