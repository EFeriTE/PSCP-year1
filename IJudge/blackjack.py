"""blackjack"""
def bj():
    """Jack Giant Killer"""
    cards = int(input())
    card_value = 0
    card_a = 0
    for _ in range(cards):
        card_pick = input()
        if card_pick == "A":
            card_value += 11
            card_a += 1
        elif card_pick in "JQK":
            card_value += 10
        else:
            card_value += int(card_pick)
    while card_value > 21 and card_a:
        card_value -= 10
    print(card_value)
bj()
