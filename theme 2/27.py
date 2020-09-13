x1 = input()
y1 = input()
a1 = input()
b1 = input()
x2 = input()
y2 = input()


 
t1 = x1 * 60 + y1
t2 = a1 * 60 + b1
t0 = 2 * t1 - t2
t3 = x2 * 60 + y2
t_real = t3 * 2 - t0 + 1440
b2 = t_real % 60
a2 = t_real / 60 % 24
print(a2, ":", b2)