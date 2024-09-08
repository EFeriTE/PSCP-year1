"""Rectangle"""
def start():
    """input"""
    height = int(input())
    wide = int(input())
    calulator(height,wide)
    return(height,wide)

def calulator(height,wide):
    """calculator"""
    area = height * wide
    print(area)
    around = (height + wide) * 2
    print(abs(around))

start()
