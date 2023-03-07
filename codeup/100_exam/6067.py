i = int(input())
if i % 2 == 0 and i < 0:
    print("A")
if i % 2 != 0 and i < 0:
    print("B")
if i % 2 == 0 and i > 0:
    print("C")
if i % 2 != 0 and i > 0:
    print("D")