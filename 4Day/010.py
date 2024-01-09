# 숫자를 입력받아 양수, 음수, 0을 출력
num = int(input('숫자를 입력하세요 -> '))
if num==0:
    print('0입니다.')
elif num <0:
    print('음수입니다.')
elif num > 0:
    print('양수입니다.')

# 점수를 입력받아 70~90점이면 "추천대상", 아니면
# "대상 아님"이라고 출력

point = int(input('점수를 입력하세요 -> '))
if point < 70:
    print('대상 아님')
elif point >= 70 and point <= 90:
    print('추천 대상')