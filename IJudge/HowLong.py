"""WHY"""
def long_navigator(checker):
    """Harder"""
    check = 0
    for _ in str(checker):
        check += 1
    return check

def main():
    """why dont use"""
    number = abs(int(input()))
    print(long_navigator(number))

main()
