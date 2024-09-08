"""BrickBridgr"""
def brick():
    """BrickBridgr"""
    small_have = int(input())
    big_have = int(input())
    goal = int(input())
    big_used = goal//5
    if big_used > big_have:
        big_used = big_have
    small_used = goal-(big_used*5)
    if small_used > small_have:
        print("-1")
    else:
        print(small_used)
brick()
