# price = [500, 5000, 8900, 1800, 2500]
# fruit = ['사과', '파인애플', '수박']

# print(price, end=' ')
# print(type(price))


# print(fruit, end=' ')
# print(type(fruit))


# fruitprice = ['사과', 1500, '수박', 8900]
# print(fruitprice)
# print(type(fruitprice[0]), end=' ')
# print(type(fruitprice[1]), end=' ')
# print(type(fruitprice[2]), end=' ')
# print(type(fruitprice[3]), end=' ')

# a = []
# b = list()
# print(type(a), end=' ')
# print(type(b))

# num = list(range(1, 21, 2))
# print(num)
# print(type(num))

# a = list("Korea")
# print(a)
# print(type(a))

# print(len(num))
# print(len(a))

# score = [88, 95, 70, 100, 99]
# print(score[0], end=" ")
# print(score[1], end=" ")
# print(score[2], end=" ")
# print(score[3], end=" ")
# print()
# print(score[-1], end=" ")
# print(score[-2], end=" ")
# print(score[-3], end=" ")
# print(score[-4], end=" ")

# score = [88, 95, 70, 100, 99]
# score[0] = 10
# score[1] = 20
# score[2] = 30

# score[-2] = 40
# score[-1] = 50
# print(score)

# animals = ['토끼', '거북이', '사자', '호랑이']
# i=0
# while i < len(animals):
#     print(animals[i])
#     i += 1

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num[2:5:1])
# print(num[1:7:2])
# print(num[0:5:2])

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num[0:5:1])
# print(num[0:7:2])
# print(num[0:5:2])

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num[2:10:1])
# print(num[1:2:1])
# print(num[7:10:1])

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num[2:5])
# print(num[1:7])
# print(num[0:5])

# fruit = ['사과', '오렌지', '딸기', '포도', '감', '키위', '멜론' ,'수박']

# print(fruit)
# print(fruit[0])
# print(fruit[1:4])
# print(fruit[2:])
# print(fruit[-1])
# print(fruit[-4:-2])
# print(fruit[-3:])

# my_list = list("PythonIsFun!")
# print(my_list)
# print(my_list[5:11])
# print(my_list[-5:-2])
# print(my_list[:4])
# print(my_list[8:])

# s = "python"
# print(s[2])
# print(s[-2])
# print(s[1:4])

# file = "20210505-104830.jpg"
# print(f"촬영날짜: {file[4:6]}월 {file[6:8]}일")
# print(f"촬영시간: {file[9:11]}시 {file[11:13]}분")
# print(f"확장자: {file[16:]}")

# s = "차종: 코란도C, 제조사: 쌍용, 배기량: 1998"
# print(s[15:17])

# jumin = "901231-1914983"
# year = jumin[0:2]
# if int(jumin[7]) % 2 == 0:
#     gender = "여자"
# else:
#     gender = "남자"
# print(f"{year}년생 {gender}입니다.")

# nums = [1,2,3,4]
# nums.append(5)
# print(nums)

# nums.insert(2, 99)
# print(nums)

# list1 = [1,2,3,4,5]
# list2 = [10, 11]
# list1.extend(list2)
# print(list1)

# score = [88, 95, 70, 100, 99]
# print("100의 위치: ", score.index(100)+1)
# print(score.pop())
# print(score.pop())
# print(score.pop(1))
# print(score)

# score = [88, 95, 70, 100, 99]
# score.remove(99)
# print("구십구 삭제 후 : ", score)
# score.sort()
# print("리스트 정렬 후 : ", score)
# score.sort(reverse=True)
# print("거꾸로 정렬 후 : ", score)
# score.clear()
# print("리스트 삭제 후 : ", score)

# list1 = ['a', 'bb', 'c', 'd', 'aaa', 'c', 'ddd', 'aaa', 'b', 'cc', 'd', 'aaa',]
# length = len(list1.count('aaa'))
# print(length)

# mylist = ['사과', '바나나', '파인애플']
# mylist.append("키위")
# mylist.append("배")
# for a in mylist:
#     print(a)

# scores = []

# while True:
#     score = int(input("성적을 입력하세요(종료: -1)"))
#     if score == -1:
#         break
#     else:
#         scores.append(score)
# print(scores)

# num = []
# for i in range(5):
#     num.append(int(input("숫자를 입력하세요")))
# num.sort()
# print(num)

# emails = [["kim", "naver.com"], ["hwang", "hanmail.net"], ["lee", "korea.com"], ["choi", "gamil.com"]]

# email_new = []
# for email in emails:
#     email_new.append(email[0] + "@" + email[1])

# print(email_new)

# fruits = ["apple", "orange", "banana"]

# for fruit in fruits:
#     print(fruit)

# s = "Hello"
# for i in s:
#     print(i, end=" ")

# colors = ["red", "green", "blue", "yellow"]
# for color in colors:
#     print("i love " + color)

# numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]
# sum=0
# for number in numbers:
#     sum = sum + number
# print("합계 ",sum)

# score = [1, 3, 5, 7, 9, 11, 13]
# cnt = 0
# for num in score:
#     if num < 10:
#         cnt += 1
#         print(num, end=" ")
# print("10보다 작은 수의 개수: ", cnt)

# questions = ["tr_in", "b_s", "_axi", "air_lane"]
# answers = ["a", "u", "t", "p"]
# count = 0
# for i in range(4):
#     ans = input(f"{questions[i]}에서 밑줄안에 들어갈 알파벳은?")
#     if ans == answers[i]:
#         print("정답입니다!")
#         count += 1
#     else:
#         print("오답입니다!")
# print("당신의 점수는 ", count)

# sum = 0
# score = list(int(input("숫자를 입력하세요: ")) for i in range(5))
# print(score)
# for i in score: sum += i
# print(f"총점은 {sum}이고 평균은 {sum / 5.0}입니다.")

# numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]

# sum = 0
# i = 0
# print("짝수 번째 요소 :", end=" ")

# while i < len(numbers):
#     if i % 2 == 1:
#         print(numbers[i], end=" ")
#         sum += numbers[i]
#         i += 1
#     else:
#         i += 1   
# print()
# print("합계: ", sum)      

s = [65, 89, 100, 85, 77, 58, 79, 67, 96, 87, \
    87, 36, 82, 98, 84, 76, 63, 69, 53, 22]

soo = 0
woo = 0
mi = 0
yang = 0
ga = 0

i = 0
while i < len(s):
    if s[i] >= 90:
        soo += 1
    elif s[i] >= 80:
        woo += 1
    elif s[i] >= 70:
        mi += 1
    elif s[i] >= 60:
        yang += 1
    else:
        ga += 1
    i += 1

print("수 : ", soo, "\n우 : ", woo, "\n미 : ", mi, "\n양 : ", yang,"\n가 : ", ga,)