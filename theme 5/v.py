def print_ans_and_exit(ans):
    print(' '.join(map(str, ans)))
    exit()


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == 0 and c == 0:
    # by = e; dy = f; x - любой
    if b == 0 and d == 0:
        # 0 = e; 0 = f
        print_ans_and_exit([5] if e == 0 and f == 0 else [0])
    if b == 0:
        # 0 = e; dy = f
        print_ans_and_exit([4, f / d] if e == 0 else [0])
    if d == 0:
        # by = e; 0 = f
        print_ans_and_exit([4, e / b] if f == 0 else [0])
    # by = e; dy = f
    print_ans_and_exit([4, e / b] if e / b == f / d else [0])

if a == 0:
    a, b, e, c, d, f = c, d, f, a, b, e

m = c / a
c -= m * a
d -= m * b
f -= m * e

# ax+by=e; 0=f; a != 0, c = 0
if d == 0:
    if f != 0:
        print_ans_and_exit([0])
    # ax=e
    if b == 0:
        print_ans_and_exit([3, e / a])
    # ax+by=e
    print_ans_and_exit([1, -a / b, e / b])

# ax+by=e; dy=f; a != 0, d != 0
y = f / d
x = (e - b * y) / a
print_ans_and_exit([2, x, y])
