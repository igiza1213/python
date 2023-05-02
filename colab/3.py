h = int(input("현재 시: "))
m = int(input("현재 분: "))
h = (h + m // 60) % 24
m = m % 60
print(f"20분 뒤는 {h}시 {m}분 입니다.")

