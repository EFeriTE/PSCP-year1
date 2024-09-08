"""weightstation"""
def station():
    """weight"""
    avg,w1,w2,w3 = float(input()),float(input()),float(input()),float(input())
    bavg = avg/2
    aavg = avg+bavg
    broke = (w1+w2+w3)/4
    if w1+w2+w3+broke > 15000:
        print("Overweight")
    elif (bavg > w1) or (w1 > aavg) or (bavg > w2) or (w2 > aavg) or (bavg > w3) or (w3 > aavg):
        print("Unblance")
    else:
        print(f"Pass {broke:.2f}")

station()
