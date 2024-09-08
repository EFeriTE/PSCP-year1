"""PlanC"""
def plan():
    """main"""
    option = input()
    number1,number2,number3 = float(input()),float(input()),float(input())
    if option == "Descend":
        if number1 > number2 and number1 > number3:
            print(f"{number1:.2f},",end =" ")
            if number2 > number3:
                print(f"{number2:.2f}, {number3:.2f}",end="")
            else:
                print(f"{number3:.2f}, {number2:.2f}",end="")
        elif number2 > number1 and number2 > number3:
            print(f"{number2:.2f}",end =" ")
            if number1 > number3:
                print(f"{number1:.2f}, {number3:.2f}",end="")
            else:
                print(f"{number3:.2f}, {number1:.2f}",end="")
        elif number3 > number1 and number3 > number2:
            print(f"{number3:.2f}",end =" ")
            if number2 > number1:
                print(f"{number2:.2f}, {number1:.2f}",end="")
            else:
                print(f"{number1:.2f}, {number2:.2f}",end="")

    elif option == "Ascend":
        if number1 < number2 and number1 < number3:
            print(f"{number1:.2f},",end =" ")
            if number2 < number3:
                print(f"{number2:.2f}, {number3:.2f}",end="")
            else:
                print(f"{number3:.2f}, {number2:.2f}",end="")
        elif number2 < number1 and number2 < number3:
            print(f"{number2:.2f}",end =" ")
            if number1 < number3:
                print(f"{number1:.2f}, {number3:.2f}",end="")
            else:
                print(f"{number3:.2f}, {number1:.2f}",end="")
        elif number3 < number1 and number3 < number2:
            print(f"{number3:.2f}",end =" ")
            if number2 < number1:
                print(f"{number2:.2f}, {number1:.2f}",end="")
            else:
                print(f"{number1:.2f}, {number2:.2f}",end="")

plan()
