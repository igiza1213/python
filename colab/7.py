age = int(input("Enter your age: "))
if age <= 7:
    print("어린이")
elif age <= 13:
    print("초등학생 ")
elif age <= 16:
    print("중학생")
elif age <= 19:
    print("고등학생")
else:
    print("성인")