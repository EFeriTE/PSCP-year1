"""Atikasurin"""
def main():
    """input"""
    year_input = int(input())
    if year_input < 0:
        print("No")
    elif not year_input % 4:
        if not year_input % 100:
            if not year_input % 400:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    else:
        print("No")
main()
