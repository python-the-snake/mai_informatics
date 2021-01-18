def move(n, start, finish):
    if n > 0:
        move(n - 1, start, finish)
        print(n, start, 2)
        move(n - 1, finish, start)
        print(n, 2, finish)
        move(n - 1, start, finish)


n = int(input())
move(n, 1, 3)
