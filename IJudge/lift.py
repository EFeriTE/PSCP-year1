"""elevator"""
def lift():
    """lift"""
    people,makweight = int(input()),float(input())
    allweigth = 0
    age_safe = 1
    for _ in range(people):
        age = int(input())
        weight = float(input())
        allweigth += weight
        if age < 12:
            age_safe -=1
        if age >= 12:
            age_safe = 100
    if age_safe >= 1 and allweigth <= makweight:
        print("Safe")
    else:
        print("Not Safe")
lift()
