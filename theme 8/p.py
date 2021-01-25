def rev():
    x = int(input())
    if x != 0:
        rev()
    print(x)


rev()
