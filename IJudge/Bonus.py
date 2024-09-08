"""Bonus"""
def bonus():
    """finder"""
    salary,year,months = int(input()),int(input()),int(input())
    if months >= 10:
        year += 1
    if year > 20:
        year = 20

    if salary * year > 1000000:
        print("1000000")
    elif salary * year < 5000:
        print("5000")
    else:
        print(salary * year)
bonus()
