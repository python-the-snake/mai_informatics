n = int(input())

sum1 = 0
for i in range(1, n):
    sum1 += i * (i + 1)
    print(i, i + 1, sep="*", end="+" if (i + 1) != n else "")
print("=", sum1, sep="")
