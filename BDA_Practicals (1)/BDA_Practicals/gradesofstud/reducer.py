import sys

for line in sys.stdin:
    name, marks = line.strip().split('\t')
    marks = int(marks)
    
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    print(f"{name}\t{grade}")

    