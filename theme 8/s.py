def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish
        move(n - 1, start, temp)
        print(n, start , finish)
        move(n - 1, temp, finish)

n = int(input())
move(n, 1, 3)