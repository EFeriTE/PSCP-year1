"""grade"""
import math
def grade():
    """A pls"""
    subjects = int(input())
    grades = 0
    for _ in range(subjects):
        score = float(input())
        if  95 <= score <= 100:
            grades += 4
        elif 90 <= score < 95:
            grades += 3.5
        elif 85 <= score < 90:
            grades += 3
        elif 80 <= score < 85:
            grades += 2.5
        elif 75 <= score < 80:
            grades += 2
        elif 70 <= score < 75:
            grades += 1.5
        elif 65 <= score < 70:
            grades += 1
        elif 60 <= score < 65:
            grades += 0.5
        elif 0 <= score < 60:
            grades += 0
    gpa = grades/subjects
    gpax = math.floor(gpa * 100) / 100
    print(f"{gpax:.2f}")

grade()
