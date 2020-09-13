A = int(input())
B = int(input())
A1 = A // B
A2 = A % B
A3 = 0**(A - A2)
B1 = B // A
B2 = B % A
B3 = 0**(B - B2)
Max = A1 * B2 + A2 * B1 + B2 * A3 + A2 * B3 + A * A3**B3 * B3**A3
print(Max)