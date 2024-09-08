"""christ"""
def christmas():
    """Tree"""
    leaf_n = int(input())
    ton_k = int(input())

    for i in range(leaf_n):
        spaces = leaf_n - i - 1
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)

    for _ in range(ton_k):
        print(" " * (leaf_n - 2) + "---")
christmas()
