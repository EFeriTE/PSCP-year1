"""Bad"""
def swap():
    """Keyboard"""
    check_word = str(input())
    new_word = check_word.replace("o","@'")
    check_word = new_word.replace("i","|")
    new_word = check_word.replace("O","^")
    check_word = new_word.replace("I","&")
    new_word = check_word.replace("@'","i")
    check_word = new_word.replace("|","o")
    new_word = check_word.replace("^","I")
    check_word = new_word.replace("&","O")
    print(check_word)
swap()
