n = int(input())
a = int(input())

s = 0
for i in range(n, -1, -1):
    s = i * a + s ** 0.5

print(s)
