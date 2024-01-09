numbers = [1,3,5,7]

# 그 숫자가 numbers에 있는지 (True/False) 출력
num=5
# print(num in numbers)

# 한 번만 찾으면 성공, 실패는 numbers의 모든 값에 대해서 못 찾아야한다
# 성공과 실패의 조건이 다르다 -> if~ else~ 가 아니다
is_find = False
for item in numbers:
    if item==num:
        print(True)
        is_find=True
if is_find==False:
    print(False)