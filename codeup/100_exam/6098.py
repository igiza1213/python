a = [[0] * 10 for _ in range(10)]

for i in range(10):
    a[i] = list(map(int, input().split()))

x = y = 2

while True:
    if a[x-1][y-1] == 2:
        a[x-1][y-1] = 9
        break
    else:
        a[x-1][y-1] = 9
    if a[x-1][y] == 1:
        if a[x][y-1] == 1:
            break
        else:
            x += 1
    else:
        y += 1

for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print(end='\n')

