a, b, c = map(int, input().split())
if(a>b):
    a = b
print(a if a<c else c)

