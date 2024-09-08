"""Milk"""
def milky():
    """cow"""
    a_price = float(input())
    b_caps = int(input())
    c_free = int(input())
    d_money = float(input())
    bottle = d_money // a_price
    caps = bottle

    if not b_caps:
        bottle = d_money // a_price

    else:
        while caps >= b_caps:
            free_bottles = (caps // b_caps) * c_free
            bottle += free_bottles
            caps = caps % b_caps + free_bottles
    print(int(bottle))

milky()
