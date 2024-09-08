"""Post"""
def konsong():
    """Office"""
    envelop,package = int(input()),int(input())
    price_envelop = envelop * 13
    price_package = package * 15
    for _ in range(envelop):
        envelop_weight = float(input())
        if 10 >= envelop_weight:
            price_envelop += 16
        elif 20 >= envelop_weight:
            price_envelop += 18
        elif 100 >= envelop_weight:
            price_envelop += 23
        elif 250 >= envelop_weight:
            price_envelop += 28
        elif 500 >= envelop_weight:
            price_envelop += 33
        elif 1000 >= envelop_weight:
            price_envelop += 48
        elif 2000 >= envelop_weight:
            price_envelop += 68

    for _ in range(package):
        package_weight = float(input())
        if 500 >= package_weight:
            price_package += 45
        elif 1000>= package_weight:
            price_package += 55
        elif 2000 >= package_weight:
            price_package += 70
    print(price_envelop + price_package)
konsong()
