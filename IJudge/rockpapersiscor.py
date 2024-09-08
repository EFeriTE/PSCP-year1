"""RPS"""
def rps():
    """paooyingcub"""
    matchs = input()
    mrange = len(matchs)
    a_score = 0
    b_score = 0
    for i in range (1,mrange,2):
        round = matchs[i-1]+matchs[i]
        if round in ("RS","SP","PR"):
            a_score += 1
        elif round in ("RP","SR","PS"):
            b_score += 1
    if a_score > b_score:
        print(f"A win {a_score} - {b_score}")
    elif b_score > a_score:
        print(f"B win {b_score} - {a_score}")
    else:
        print(f"DRAW {a_score}")
rps()
