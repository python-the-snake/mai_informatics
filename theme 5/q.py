n = int(input())
x = float(input())
sum_ = 0
fact = 1
p = 1

for i in range(n + 1):
    sum_ += p / fact
    p *= x
    fact *= (i + 1)
print(sum_)
