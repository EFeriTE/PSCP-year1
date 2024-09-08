"""second"""
def second():
    """converter"""
    k = int(input())
    s = int(input())
    m = int(input())
    h = int(input())
    minutes = k//s
    sec = k%s
    hours = minutes//m
    minutes = minutes%m
    hours = hours%h
    print(f"{hours}:{minutes}:{sec}")
second()
