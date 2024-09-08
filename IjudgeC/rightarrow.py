"""Right"""
def rarrow():
    """Arrow"""
    k = int(input())
    n = int(input())
    mid = n//2

    for i in range(mid):
        spaces = i
        print(" " * spaces + "*" * k)

    print(" " * mid + "*" * k)

    for i in range(mid - 1, -1, -1):
        spaces = i
        print(" " * spaces + "*" * k)
rarrow()
