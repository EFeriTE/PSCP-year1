"""Left"""
def larrow():
    """Arrow"""
    k = int(input())
    n = int(input())
    mid = n//2

    for i in range(mid):
        spaces = mid - i
        print(" " * spaces + "*" * k)

    print("*" * k)

    for i in range(mid - 1, -1, -1):
        spaces = mid - i
        print(" " * spaces + "*" * k)
larrow()
