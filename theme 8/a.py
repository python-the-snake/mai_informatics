import math
 
def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)
 
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print("{:g}".format(distance(x1, y1, x2, y2)))
