# 75, 80, 70 이라는 국어점수가 있다 -> 집합타입(seouence)
# 값 하나를 저장 : int, float, str, bool
# 값 여러 개를 저장 : list, tuple, dictionary, set
kor75 = 75
kor80 = 80
kor70 = 70
print(kor75)
print(kor80)
print(kor70)

kor=[75,80,70]
# kor의 타입 츨력
print(type(kor))
print(kor[0])
print(kor[1])
print(kor[2])

# 조건문, 반복문
# kor 리스트의 원소를 하나씩 꺼내서 item에 담는다
for item in kor:
    print(item)

# 리스트는 변경 가능하고, 튜플은 변경불가능
리스트 = ["사과", "귤", "수박"]
튜플 = ("사과", "귤", "수박")

# Create Read Update Delete

for aaa in 리스트:
    print(aaa)
