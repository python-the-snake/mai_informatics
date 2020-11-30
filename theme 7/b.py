from math import sqrt
n = int(input())
p = 2
while n % p != 0 and p < sqrt(n) + 1:
    p += 1
print(p if p < sqrt(n) + 1 else n)