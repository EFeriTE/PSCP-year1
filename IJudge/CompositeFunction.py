"""CompositeFunction"""
def fx():
    """input"""
    x = float(input())
    functionx(x)

def functionx(x):
    """Calculator"""
    f = x * 2
    g = (x/2) + 1
    fg = (f/2) + 1
    gf = g * 2
    print(f'{gf:.2f}')
    print(f'{fg:.2f}')

fx()
