n = int(input())
a = list(map(int, input().split()))
for i in range(1, 24):
    print(a.count(i), end=" ")
