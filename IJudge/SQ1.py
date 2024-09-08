"""main"""
def main():
    """input"""
    number = int(input())
    for _ in range(1, number+1):
        sq(number)
        print()

def sq(number):
    """loop"""
    print(*(_ for _ in range(1, number+1)), sep = " ", end ="")

main()
