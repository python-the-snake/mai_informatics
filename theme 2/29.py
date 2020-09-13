n, k, m = map(int, input().split())

counter = 0

while k < n:

   ost = n // k

   counter += ost * (k // m)

   n -= ost * (k // m) * m

print(counter)