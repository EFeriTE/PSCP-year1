"""donut"""
def donut():
    """donut"""
    price = int(input())
    buy = int(input())
    free = int(input())
    need = int(input())
    bought = 0
    paid = 0
    full_set = buy + free
    bought_set = need // full_set

    paid = bought_set * (price * buy)
    bought = bought_set * full_set

    while bought < need:
        if need - bought >= buy:
            bought += (buy+free)
            paid += buy*price
        else:
            bought += 1
            paid += price
    print(paid, bought)
donut()
