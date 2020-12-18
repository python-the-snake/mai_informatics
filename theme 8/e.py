def func(x, y, xc, yc, r):
    return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r


if __name__ == '__main__':
    x = float(input())
    y = float(input())
    xc = float(input())
    yc = float(input())
    r = float(input())
    func(x, y, xc, yc, r)
    if func(x, y, xc, yc, r):
        print("YES")
    else:
        print("NO")
