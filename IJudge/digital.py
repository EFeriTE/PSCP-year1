"""digital"""
def forthai():
    """wallet"""
    name,thaimhai,stayhome = input(),input(),input()
    age,salary,saved = float(input()),float(input()),float(input())
    if thaimhai in ("Yes","True") and stayhome in ("Yes","True") \
and age >= 16 and  saved <= 500000 and salary <= 840000:
        print(f"Congratulations! {name} is qualified to receive a digital \
wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
forthai()
