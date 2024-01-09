# 몇 일인지 입력받아 몇 개월 며칠인지 출력
# 333일 -> 11개월 3일

input_day = int(input('날짜 : '))
month = input_day//30
day = input_day%30
print(f'{month}개월 {day}일')

# 코드에 값이 직접 나타나는 것 : literal
# 안 바뀌는 값 : 상수
# 상수는 대문자로 입력 (바꾸면 바꿀 수 있지만 안 바꾸기로 약속된 것)
minutes = 5
seconds = 10
SECONDS_PER_MINUTE = 60
result = minutes * SECONDS_PER_MINUTE + seconds
print(result)

input_day = int(input('날짜 : '))
DAY_PER_MONTH = 30
month= input_day//DAY_PER_MONTH
day = input_day%DAY_PER_MONTH
print(f'{month}개월 {day}일')
