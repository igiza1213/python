# animals = ['토끼', '거북이', '사자', '호랑이']
# for i in range(0, 4) :
#     print(animals[i])
# for i in animals :
#     print(i)

# nums = [1,2,3,4]
# nums.append(5) # 추가
# print(nums)

# nums.insert(2,99) # 삽입
# print(nums)

# list1 = [1,2,3,4,5]
# list2 = [10, 11]
# list1.extend(list2) # 합치기
# print(list1)

# score = [88, 95, 70, 100, 99]
# print("100의 위치: ", score.index(100)+1)

# print(score.pop()) # 마지막 요소 꺼내기
# print(score.pop()) # 마지막 요소 꺼내기
# print(score.pop(1)) # 인덱스 1번 요소 꺼내기
# print(score)

score = [int(input("성적입력 : ")) for i in range(5)]
print(score)
sum = 0
for i in score: sum += i 
print(f"총점은 {sum}이고 평균은 {round(sum / 5, 1)}")