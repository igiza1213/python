# name  = input("이름을 입력하세요")
# hour = int(input("일주일간 일한 시간을 입력하세요"))
# if hour > 40:
#     over = hour - 40
#     print(f"초과 시간 : {over}")
#     print(f"{name} 님의 주급은 {12000 * 40 + 1200 * over * 1.5}입니다.")
# else:
#     print(f"{name} 님의 주급은 {12000 * hour}입니다.")

# print ((3 == 3) and (4 != 3))
# print ((3 == 3) or (4 != 3))
# print(not(4 != 3))

# a = int(input("a입력:"))
# b = int(input("b입력:"))
# if a == 3 and b == 4:
#     print("ok")
# if a == 3 or b == 4:
#     print("okay")

# x = int(input("숫자입력:"))
# if x > 10 and x % 2 == 0:
#     print("10 초과 짝수")

# i = int(input("필기 성적을 입력하세요 : "))
# j = int(input("실기 성적을 입력하세요 : "))
# if i >= 80 and j >= 80:
#     print("합격!")
# else:
#     print("불합격!")

# age = int(input("나이를 입력하세요 : "))
# if age < 7 or age > 65:
#     print("입장료는 무료입니다.")
# else:
#     print("입장료는 3000원입니다.")

# age = int(input("나이를 입력하세요 : "))
# height = int(input("키를 입력하세요 : "))
# if age >= 10 and height >= 150:
#     print("탈 수 있다")
# else:
#     print("탈 수 없다")

# id = input("아이디를 입력하세요 : ")
# level = int(input("회원 레벨을 입력하세요 : "))

# if level == 1 or id == "admin":
#     print("admin")
# else:
#     print("user")

i = int(input("정수를 입력하세요 : "))
if i > 0 and i < 100:
    print(f"{i}는 1~100 사이의 정수입니다.")
