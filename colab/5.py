id = input("아이디를 입력하세요: ")
level = int(input("레벨을 입력하세요: "))
if id == "admin" or level == 1:
    print("관리자입니다.")
else:
    print("관리자가아닙니다.")
