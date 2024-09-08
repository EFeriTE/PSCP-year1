"""why physics"""

def velocity_input():
    """input"""
    displacement = float(input())
    time = float(input())
    cal(displacement,time)
    return displacement,time

def cal(displacement,time):
    """cal"""
    velo = displacement/time
    print(abs(velo))

velocity_input()
