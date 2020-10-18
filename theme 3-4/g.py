n = int(input())
k = int(input())
a = 1
b = 1
c = 1
for i in range(1, n + 1):
    a = a * i
for i in range(1, k + 1):
    b = b * i
for i in range(1, (n-k) + 1):
    c = c * i
print(a//b//c)
