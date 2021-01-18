ind = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[ind]:
        ind = i
print(a[ind], ind)