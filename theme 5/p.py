n = int(input())

s = 0
for i in range(1, 2 * n + 2, 4):
    s += 1 / i
for i in range(3, 2 * n + 2, 4):
    s -= 1 / i

print(s * 4)
