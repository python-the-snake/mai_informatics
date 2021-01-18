def IsPrime(x):
    if x == 2:
        return True

    i = 2
    while x % i != 0:
        if i >= x ** 0.5:
            return True
        i += 1
    return False

x = int(input())


if IsPrime(x):
    print("YES")
else:
    print("NO")