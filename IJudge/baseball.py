"""homerun"""
def home():
    """run"""
    times,ranges = int(input()),float(input())
    score = 0
    for _ in range(times):
        fields = float(input())
        if fields < ranges:
            score += 1
    print(score)
home()
