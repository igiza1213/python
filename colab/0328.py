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

# i = int(input("정수를 입력하세요 : "))
# if i > 0 and i < 100:
#     print(f"{i}는 1~100 사이의 정수입니다.")

# month = 3
# if 3 <= month <= 5:
#     print("봄입니다.")
# elif 6 <= month <= 8:
#     print("여름입니다.")
# elif 9 <= month <= 11:
#     print("가을입니다.")
# else:
#     print("겨울입니다.")

# prise = int(input("구매금액: "))
# if prise >= 50000:
#     print("무료배송")
# elif prise >= 20000:
#     print("2500원 추가")
# else:
#     print("불가능 합니다.")

# score = int(input("점수를 입력하세요:"))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")

# temp = int(input("온도를 입력하세요: "))
# if temp >= 100:
#     print("기체입니다")
# elif temp >= 0:
#     print("액체입니다")
# else:
#     print("고체입니다")

# eng = int(input("영어 점수: "))
# math = int(input("수학 점수: "))
# if eng >= 80 and math >= 80:
#     print("합격입니다")
# elif eng >= 80 or math >= 80:
#     print("재시험의 기회")
# else:
#     print("탈락")

# satisfaction = int(input("만족도 :"))
# prise = int(input("가격 :"))
# if satisfaction == 1:
#     print("팁 : ", prise * 0.2)
# elif satisfaction == 2:
#     print("팁 : ", prise * 0.1)
# else:
#     print("팁 : ", prise * 0.05)

# menu = int(input("메뉴를 선택하세요 : "))
# if menu == 1:
#     prise = int(input(("당신은 떡볶이를 선택하셨군요!\n몇인분 : "))) * 3000
#     print("총 가격: ", prise)
# elif menu == 2:
#     prise = int(input(("당신은 김밥를 선택하셨군요!\n몇인분 : "))) * 2500
#     print("총 가격: ", prise)
# elif menu == 3:
#     prise = int(input(("당신은 튀김를 선택하셨군요!\n몇인분 : "))) * 3500
#     print("총 가격: ", prise)
# else:
#     print("1 2 3중에 선택하세요")

# weight = int(input("몸무게를 입력하세요 : "))
# height = int(input("키를 입력하세요 : "))
# bmi = weight / (height**2)

# if bmi > 25:
#     temp = "비만"
# elif bmi > 15:
#     temp = "과체중"
# else:
#     temp = "정상"
# print(f"당신의 bmi지수는 {bmi}이며 {temp}입니다.")

# weghit = int(input("몸무게를 입력하세요 : "))
# height = int(input("키를 입력하세요 : "))
# age = int(input("나이를 입력하세요 : "))
# sex = input("성별를 입력하세요 : 남자/여자")
# if sex == "남자":
#     print(f"당신의 기초 대사량은 {66.47 + (13.75 * weghit) + (5 * height) - (6.76 * age)}")
# else:
#     print(f"당신의 기초 대사량은 {655.1 + (9.56 * weghit) + (1.85 * height) - (4.68 * age)}")

# x = 17
# if x > 10 :
#   if x % 2 == 0:
#     print("10초과 짝수")
#   else :
#     print("10초과 홀수")
# else :
#   print("10 이하")

# userid = input("아이디를 입력하세요: ")
# level = int(input("회원 레벨을 입력해 주세요 : "))
# if userid == "admin" :
#   print("모든 콘텐츠 이용 가능")
# elif 2 <= level <= 7 :
#   print("일부 콘텐츠 이용 가능")

# year = int(input("현재년을 입력해 주새요: "))
# month = int(input("현재월을 입력해 주새요: "))
# day = int(input("현재일을 입력해 주새요: "))
# birthYear = int(input("출생년을 입력해 주새요: "))
# birthMonth = int(input("출생월을 입력해 주새요: "))
# birthDay = int(input("출생일을 입력해 주새요: "))

# if birthMonth < month :
#   age = year - birthYear

# if birthMonth == month :
#   if birthDay < day :
#     age = year - birthYear
#   else :
#     age = year - birthYear - 1
# else :
#   age = year - birthYear - 1

# print("---------------------------------")

# print("오늘 날짜 : ", year, "년 ", month , " 월", day , "일")
# print("생년 월일 : ", birthYear ,"년 ", birthMonth , " 월", birthDay , "일")

# print("---------------------------------")

# print("만 나이 : ", age, "세")
