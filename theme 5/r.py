n = int(input())
x = float(input())

s = 1
current_element = 1
for i in range(n):
    current_element *= x * x
    current_element /= (i * 2 + 1) * (i * 2 + 2)
    if i % 2 == 0:
        s -= current_element
    else:
        s += current_element

print(s)
