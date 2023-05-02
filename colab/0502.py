# for dan in range(2,10):
#   print(dan, "단")
#   for i in range(2, 10):
#     print(dan, "*", i, "=", dan * i)


# n = int(input("원하는 단은? "))
# dan = 2
# while dan < 10:
#   print(dan, "단")
#   hang = 2
#   while hang < 10:
#     print(dan, "*", hang, "=", dan * hang)
#   dan += 1

# for i in range(1, 5):
#     for i in range(1, 5):
#         print("*")
#     print()

# for i in range(7):
#     for j in range(7):
#         if i == j or i + j == 6:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# number = input("숫자를 입력하세요: ")
# total = 0
# for digit in number:
#     if int(digit) % 2 == 1:
#         total += 1
# print("홀수의 개수:", total)

# for i in range(5):
#     for j in range(10):
#         print("*", end=" ")
#     print()

# for i in range(5):
#     for j in range(0, i):
#         print("*", end=" ")
#     print()

# for i in range(6):
#     for j in range(0, 5-i):
#         print(" ", end=" ")
#     for k in range(0, i):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print(i, end=" ")
#     print()

# n1 = int(input("첫 수를 입력하세요: "))
# n2 = int(input("끝 수를 입력하세요: "))
# n = int(input("합계를 구하고자 하는 배수를 입력하세요: "))
# sum = 0
# for i in range(n1,n2+1):
#     if i % n == 0:
#         sum += i

# print(f"{n1}부터까지의 {n2}의 {n}의 배수의 합은 {sum}")

n = int(input("n을 입력하세요: "))
sum = 0
for i in range(n+1):
    temp=0
    for j in range(1,i):
        temp = i + 1
        sum += i

print("수열 Sn = ", sum)