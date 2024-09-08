"""long"""
def finder(value):
    """checker"""
    return 50 <= value <= 70

def check_chickens1():
    """15"""
    return (
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input()))
    )

def check_chickens2():
    """9"""
    return (
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input())) +
        finder(int(input()))
    )

def main():
    """main"""
    number = check_chickens1() + check_chickens2()
    print(number)

main()
