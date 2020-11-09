a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == 0:
    y = e / b
    x = (f - d * y) / c
    print(x, y)
else:
    m = c / a
    c -= m * a
    d -= m * b
    f -= m * e

    y = f / d
    x = (e - b * y) / a
    print(x, y)