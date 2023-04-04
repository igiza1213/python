# import datetime 
# from pytz import timezone

# now = datetime.datetime.now(timezone('Asia/Seoul'))

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# import datetime 
# from pytz import timezone
# now = datetime.datetime.now(timezone('Asia/Seoul'))
# month = now.month



# if month > 8:
#     print(f"이번 달은 {month}로 가을입니다!")
# elif month > 5:
#     print(f"이번 달은 {month}로 여름니다!")
# elif month > 2:
#     print(f"이번 달은 {month}로 봄입니다!")
# else:
#     print(f"이번 달은 {month}로 겨울입니다!")




# import random

# print(random.random())
# print(random.randrange(1, 7))
# print(random.randint(1, 6))
# print(random.choice([10, 20, 30]))

# import random
# time = random.randrange(0,24)
# ran = random.choice([True, False])
# print(f"좋은 {'아침' if time < 12 else'오후'}입니다 지금 시각은 {time} 시 입니다.\n현재 날씨가 {'화창합니다.' if ran else '화창하지 않습니다'}\n종달새가 {' 노래 합니다.' if ran else '노래하지 않습니다'}")

# x = 0
# while x < 3:
#     print("안녕하세요")
#     x += 1

# student = 1
# while student <=3:
#     print(student, "번 학생의 성적을 처리한다.")
#     student += 1

# dan = int(input("원하는 단은? "))
# i = 1
# while i < 10:
#     print(f"{dan} * {i} = {dan * i}")
#     i += 1;

# num = 1
# sum = 0
# while num < 11:
#     sum += num
#     print(f"num의 값 : {num} => 합계 : {sum}")
#     num += 1

# sum = 0
# i = 150
# while i < 301:
#     if i % 2 == 0:
#         i += 1
#         continue
#     sum += i
#     i += 1
# print("sum = ", sum)

# i = -5
# print("섭씨\t화씨")
# while i <6:
#     print(f"{i}\t{i * 9.0/5.0 + 32.0}")
#     i += 1

# sum = 1
# i = 0
# while i<10:
#     sum = sum * (10 - i)
#     i+=1

# print(f"10! = {sum}")

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print(i,end=" ")
#     i+=1