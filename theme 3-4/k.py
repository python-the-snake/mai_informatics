a, b = int(input()), int(input())
a = a + a % 2
for i in range(a, b + 1, 2):
    print(i, end=' ')
