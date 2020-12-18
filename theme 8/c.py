start = 1
end = -1


def IsPointInSquare(x, y):
    return (start >= x >= end) and (end <= y <= start)


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
