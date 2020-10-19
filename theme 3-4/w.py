a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range(1001):
    if a * x**3 + b * x**2 + c * x + d == 0:
        print(x)
