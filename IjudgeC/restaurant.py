"""Restaurant"""

def restarant():
    """promotion"""
    eaten = float(input())
    promotion = float(input())
    percent = float(input())
    more = float(input())
    sums = eaten + more
    discount = 0
    after = 0

    if eaten >= promotion:
        eaten -= eaten * (percent / 100)
    if sums >= promotion:
        discount = sums * (percent/100)
        after = sums - discount
        if after == eaten:
            print("Yes")
        elif eaten > after:
            print(f"Yes {abs(eaten - (sums - discount)):.3f}")
        elif eaten < after:
            print(f"No {abs(eaten - (sums - discount)):.3f}")
    else:
        print("Yes")
restarant()
