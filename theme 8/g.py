a = float(input())
n = float(input())


def power(a, n):
    i = 0
    while i < (n - 1):
        a *= a
        i += 1
    print(a)

print(power(a, n))


