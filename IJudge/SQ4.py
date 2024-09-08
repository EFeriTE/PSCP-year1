"""SQ4"""
def sq():
    """doubleloop"""
    num = int(input())
    start = 1
    ends = num
    for _ in range(num):
        for i in range(start,num+1):
            print(i,end=" ")
        start += ends
        num += ends
        print()
sq()
