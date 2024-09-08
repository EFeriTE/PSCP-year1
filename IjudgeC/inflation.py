"""Inflation"""
def inflation():
    """Inflation"""
    price_n = int(float(input()) * 100)
    year_k = int(input())

    while year_k:
        price_n = price_n + (price_n * 381) // 10000
        year_k -= 1
    print(f"{price_n // 100}.{str(price_n)[-2:]:02}")
inflation()
