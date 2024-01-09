리스트=[3, 'hello', 5>3, True]
튜플=tuple(리스트)

# CRUD - 삭제는 del 연산자
# method : 객체(파이썬을 구성하는 부품)에 소속된 함수
# append = method라 소속되어서만 사용 가능 / print는 그냥 사용 가능
# append와 print는 다르니까 잘 알아두기
리스트.append(100) # 맨 끝에 추가되고 신경 쓸 필요 X # create
리스트[0]=리스트[0]*10 #update
print(리스트)
del 리스트[0] #delete
print(리스트)

# 튜플. 해서 나오는 박스들은 멤버라고 부름
# __~~~__ 처럼 언더바언더바가 들어간 멤버들은 내부적으로 사용하는 거라 신경 X
# 튜플 = 읽기전용