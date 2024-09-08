"""Vote"""
def suprise():
    """suprise"""
    sumall, highest = float(input()),float(input())
    lowest = sumall - highest*2
    if lowest < 0:
        lowest = 0
    if highest - lowest <= 2:
        print("Not surprising")
    else:
        print("Surprising")
suprise()
