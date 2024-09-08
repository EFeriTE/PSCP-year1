"""LsizeNumber"""
def largest():
    """number"""
    num1,num2,num3 = str(input()),str(input()),str(input())
    set1 = int(num1 + num2 + num3)
    set2 = int(num1 + num3 + num2)
    set3 = int(num2 + num1 + num3)
    set4 = int(num2 + num3 + num1)
    set5 = int(num3 + num1 + num2)
    set6 = int(num3 + num2 + num1)
    if set1 >= set2 and set1 >= set3 and set1 >= set4 and set1 >= set5 and set1 >= set6:
        print(set1)
    elif set2 >= set1 and set2 >= set3 and set2 >= set4 and set2 >= set5 and set2 >= set6:
        print(set2)
    elif set3 >= set2 and set3 >= set1 and set3 >= set4 and set3 >= set5 and set3 >= set6:
        print(set3)
    elif set4 >= set2 and set4 >= set3 and set4 >= set1 and set4 >= set5 and set4 >= set6:
        print(set4)
    elif set5 >= set2 and set5 >= set3 and set5 >= set4 and set5 >= set1 and set5 >= set6:
        print(set5)
    elif set6 >= set2 and set6 >= set3 and set6 >= set4 and set6 >= set5 and set6 >= set1:
        print(set6)

largest()
