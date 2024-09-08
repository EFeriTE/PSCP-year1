"""SQ"""
def sq():
    """M"""
    n = int(input())
    row = 0
    column = 0
    for row in range(n):
        for column in range(n+1):
            if column in (0, n - 1, row):
                print("*", end="")
            else:
                print(" ", end="")
        print()
sq()
