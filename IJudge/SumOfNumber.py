"""Sum of number"""
def main():
    """Cauculator"""
    firstnumber = int(input())
    total = 0
    while True:
        number = int(input())
        if number == -1:
            break
        total += number
        if total == firstnumber:
            break
    print(total)

main()
