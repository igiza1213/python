import random

# k = int(input('n을 입력하시오: '))
# sum = 0
# for i in range(1, k+1):
#   temp=0
#   for j in range(1, i+1):
#     temp +=j
#   sum += temp
# print("수열 Sn = ", sum)

# max_value = 0
# a = 0
# b = 0
# for i in range(1, 100):
#   j = 100-i
#   current = i*j
#   if current > max_value:
#     max_valure = current
#     a = i
#     b = j
# print(f"최대가 되는 경우 : {a} * {b} = {max_value}")

# questions = ["s_hool", "compu_er", "deco_ation", "windo_", "hi_tory"]
# answers = ["c", "t", "r", "w", "s"]

# for i in range(len(questions)):
#     guess = input(f"{questions[i]}의 밑줄에 들어갈 알파벳은?")

#     if guess == answers[i]:
#         print("정답")
#     else:
#         print("오답")

# questions = ["school", "computer", "decoration", "window", "history"]

# cnt = 0
# for i in range(len(questions)):
#     x = random.randint(0, len(questions)-1)
#     answer = questions[i][x]
#     print("answer = ", answer)
#     questions[i] = questions[i].replace(answer, "_")
#     guess = input(f"{questions[i]}의 밑줄에 들어갈 알파벳은?")
#     if guess == answer:
#         print("정답")
#         cnt += 1  
#     else:
#         print("오답")
# print("맞춘 개수는 ", cnt, "개입니다.")
        
# n = int(input())
# for i in range(n):
#     print(" " * i + "**")

fruit = ['banana', 'pear', 'watermelon', 'strawberry', 'apple', 'mango', 'durian', 'lemon', 'orange', 'pineapple']
print(f"{fruit}중에 하나를 맞춰 보세요")
number = random.randint(0, 9)
while True:
    guess = input("Enter here: ")
    for i, j in enumerate(fruit):
        if guess == j:
            print("정답입니다.")
            break
        else:
            print("과일이 아닙니다.")
        if i < number:
            print("예측한 답이 더 앞에있습니다")
            break
        elif i > number:
            print("예측한 답이 더 뒤에있습니다")
            break

