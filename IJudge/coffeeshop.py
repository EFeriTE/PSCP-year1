"""Coffee"""
def shop():
    """Shoppee"""
    original_price,get_discount,promo_discount = float(input()),float(input()),float(input())
    needed_topromo,buy_amount = float(input()),int(input())
    pay_nopromo = original_price * buy_amount
    price_afterpromo1 = pay_nopromo
    price_afterpromo2 = pay_nopromo
    first_discount = original_price - (original_price * ((100 - get_discount) /100))
    if buy_amount >= 2:
        if buy_amount == 1:
            price_afterpromo1 = pay_nopromo - (first_discount*(buy_amount))
        else:
            price_afterpromo1 = pay_nopromo - (first_discount*(buy_amount-1))

    if pay_nopromo >= needed_topromo:
        price_afterpromo2 = pay_nopromo - (pay_nopromo - (pay_nopromo * ((100-promo_discount)/100)))

    if price_afterpromo1 < price_afterpromo2:
        print("1")
        print(f"{price_afterpromo1:.2f}")
    elif price_afterpromo1 == price_afterpromo2:
        print("2")
        print(f"{price_afterpromo2:.2f}")
    else:
        print("2")
        print(f"{price_afterpromo2:.2f}")

shop()
