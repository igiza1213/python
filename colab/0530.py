# number = [[10,20,30],[40,50,60]]

# for i in number:
#     print(i)

# for i in number[0]:
#     print(i)

# for i in number[1]:
#     print(i)

# number = [[10,20,30],[40,50,60,70,80]]
# print(number[0][0])
# print(number[0][1])
# print(number[0][2])
# print(number[1][0])
# print(number[1][1])
# print(number[1][2])
# print(number[1][3])

# for sub in number:
#     for i in sub:
#         print(i,end=" ")
#     print

# data = [[10, 20],[30,40],[50,60],[70,80]]

# for i in range(4):
#     for j in range(2):
#         print(f"data[{i}][{j}] = {data[i][j]}")

# string = [["원두커피", "라떼", "콜라"], ["우동", "국수", "피자", "파스타"]]

# for i in range(len(string)):
    # for j in range(len(string[i])):
#         print(string[i][j], end=" ")
#     print()

# data = [[10,20,30],[40,50],[60,70,80,90]]
# print(data)
# for i in range(len(data)):
#     print(data[i][0])

# score = [
#     [88,76,92,98],
#     [65,70,58,82],
#     [82,80,78,88],
# ]

# total = 0

# for i in range(len(score)):
#     totalsub = 0
#     for j in range(len(score[i])):
#         totalsub += score[i][j]
#     print(f"총점 : {totalsub} 평균 : {totalsub / 4}")
#     total += totalsub / 4
# print("전체 평균 : ", total/3)

# seats = [
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [1,1,1,0,0,0,0,0,1,0],
#     [0,0,0,0,0,1,0,0,0,0],
#     [0,1,0,0,0,1,0,1,0,0],
#     [0,0,0,0,0,0,1,0,0,0],
#     [1,0,1,0,0,0,0,0,0,1],
#         ]

# for i in range(len(seats)):
#     for j in range(len(seats[i])):
#         if seats[i][j] == 0:
#             print("%3s" %'□', end="")
#         else:
#             print("%3s" %'■', end="")
#     print()
# print('\n※ 예약 가능 : ■, 예약 불가 : □')

# score = [[96,84,80],[96,86,76],[76,95,83],[89,96,69],[83,86,79],[85,90,83]]
# i=0
# while i < len(score):
#     sum = 0
#     j=0
#     while j < len(score[i]):
#         sum += score[i][j]
#         j+=1
#     print(f"{i+1}번 학생의 총점 : {sum} 평균 : {round(sum / 3, 2)}")
#     i+=1

# score = [[96,84,80],[96,86,76],[76,95,83],[89,96,69],[83,86,79],[85,90,83]]
# for i in range(len(score)):
#     sum = 0
#     for j in range(len(score[i])):
#         sum += score[i][j]
#     print(f"{i+1}번째 학생의 합계 : {sum} 총점 : {round(sum/3, 2)}")


# [2 * n for n in range(1, 11)]

# even1 = [2*n for n in range(1,51)]
# even2 = [n for n in range(1, 101) if n%2 == 0]
# print(even1)
# print(even2)

# li = []
# for n in range(1, 10):
#     if n%3 ==0:
#         li.append(n*n)
# print(li)

# number = [1,2,3,4,5]
# result = []
# for n in number:
#     if n % 2 == 0:
#         result.append(n*2)

# =>

# number = [1,2,3,4,5]
# result = [ n*2 for n in number if n%2 == 1]
# print(result)

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# max = v[0]
# for i in range(len(v)):
#     if max < v[i]:
#         max = v[i]
# print(max)

# for i in [1,2,3]:
#     for j in ["a","b","c"]:
#         print(j * i, end=" ")

# list_a = ["I","study","python","language","!"]
# for i in list_a:
#     if len(i) >= 3:
#         print(i)

# a = input("첫번째 문자열")
# b = input("두번째 문자열")
# c = input("세번째 문자열")
# if a[-1] == b[0] and b[-1] == c[0] and c[-1] == a[0]:
#     print("good")
# else:
#     print("bad")

# a = "python"
# print(a[2:5])
# print(a[3:])
# print(a[:4])
# print(a[2:-2])
# print(a[-2:])

# s = "python"
# for c in s:
#     print(c, end=",")

# number = input("-을 포함한 휴대전화번호를 입력하세요")
# for i in number:
#     if i != "-":
#         print(i, end="")

# s = "python"
# print(len(s))
# n = "여섯글자이다"
# print(len(n))

# sentence = input("문자열 입력: ")
# cnt=0
# for c in sentence:
#     cnt += 1
#     if c == "t":
#         print(cnt)

# sentence = "Enjoy your life!"
# r_sentence = sentence[::-1].replace(" ", "-")
# print(r_sentence)

# data = input("문자열 입력")
# for i in range(len(data)-1):
#     print(data[i], data[i+1], sep = "")

# s = "차종: 코란도C, 제조사: 쌍용, 배기량: 1998"
# print(s[15:17])

# file = "20210505-104830.jpg"
# print(f"촬영날짜: {file[4:6]}월 {file[6:8]}일")
# print(f"촬영시간: {file[9:11]}시 {file[11:13]}분")
# print(f"확장자: {file[16:]}")

# yoil = "월화수목금토일"
# print(yoil[::2])
# print(yoil[::-1])

# jumin = "901231-1914983"
# year = jumin[0:2]
# if int(jumin[7]) % 2 == 0:
#     gender = "여자"
# else:
#     gender = "남자"
# print(f"{year}년생 {gender}입니다.")