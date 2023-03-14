h, w = map(int, input().split())
n = int(input())

a = [[0] * w for _ in range(h)] 
#[[0] * i for _ in range(j)] [0, 0, 0], [0, 0, 0] #(i = 3, j = 2) [[0 * i] * j]

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            a[x-1][y-1+j] = 1
        else:
            a[x-1+j][y-1] = 1
for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print(end='\n')



