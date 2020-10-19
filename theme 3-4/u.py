a = int(input())
b = int(input())

for i in range(a, b + 1):
    i = str(i)
    if i[0] == i[3] and i[1] == i[2]:
        print(i)
