a = float(input())
b = float(input())


def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    else:
        return a


print(sum(a, b))
