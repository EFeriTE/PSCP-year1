"""Timing II"""
def timing2():
    """TimingII"""
    sec = int(input())
    minute = sec // 60
    sec = sec % 60
    hours = minute // 60
    minute = minute % 60
    day = hours // 24
    hours = hours % 24
    if day >= 10000 or hours >= 100 or minute >= 100 or sec >= 100:
        print("ERR_:__:__:__")
    else:
        print(f"{day:04}:{hours:02}:{minute:02}:{sec:02}")
timing2()
