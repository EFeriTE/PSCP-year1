"""Rule"""
def rules():
    """Three"""
    piece = int(input())
    worthest = 1
    worth_price = 0
    worth_weight = 0

    for _ in range(piece):
        price = float(input())
        weight = float(input())
        worth = price/weight

        if worth < worthest:
            worthest = worth
            worth_price = price
            worth_weight = weight

        if worth == worthest and price < worth_price:
            worthest = worth
            worth_price = price
            worth_weight = weight

    print(f"{worth_price:.2f} {worth_weight:.2f}")
rules()
