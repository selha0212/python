# int, float, str, bool
print(type(True))
print(type(False))

# 비교 -> bool : >, >=, <, <=, ==, !=
print(5>3)
print(type(5>=3))
print(5<3)
print(type(5<=3))
print(5==3)
print(5!=3)

# 부정 : 참을 거짓으로, 거짓을 참으로
print(not True)
print(not 5>3)

# not이 적용하려면 참 또는 거짓이 판단되어야 함
print(5) # 단독으로 있을 때 5는 참도 거짓도 아님
print(not 5) # not가 붙으면 참거짓으로 바뀜
print(not 0)
print(0==True)
# 파이썬에서 논리연산을 사용하면 0은 거짓, 0이 아니면 참
# 파이썬에서 논리연산을 사용하면 ''은 거짓
print(not '')
print(not'hello')

# 타입은 고정된 것이 아니라 바꿀 수 있다
