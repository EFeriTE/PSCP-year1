"""SQ"""
def main():
    """main"""
    number = int(input())
    print(*(_ for _ in range(1,number+1)),sep = "_", end = "")
main()
