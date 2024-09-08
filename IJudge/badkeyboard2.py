"""bkV2"""
def bad():
    """keyboard"""
    sentence = input()
    for i in sentence:
        if i == "o":
            i = i.replace("o","i")
        elif i == "i":
            i = i.replace("i","o")
        elif i == "O":
            i = i.replace("O","I")
        elif i == "I":
            i = i.replace("I","O")
        print(i,end="")
bad()
