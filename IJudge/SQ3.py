"""SQ3"""
def row():
    """calculator"""
    number = int(input())
    for y in range(2, number+2):
        print(y, end= " ")
        for x in range(number-1):
            print(x + y + 1, end = " ")
        print()

row()
