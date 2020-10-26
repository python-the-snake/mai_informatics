a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c
x1 = (-1 * b + d ** 0.5) / (2 * a)
x2 = (-1 * b - d ** 0.5) / (2 * a)

if x1 == x2:
    print(x1)
elif x1 != x2:
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)


