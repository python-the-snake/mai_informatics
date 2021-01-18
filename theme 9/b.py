s = input()
a = [int(s) for s in s.split()]
print(*[elem for elem in a if elem % 2 == 0])
