# 1년은 몇 초인지 출력하시오
YEAR = 365
HOURS = 24
MINUTES = 60
SECONDS = 60
print(YEAR*HOURS*MINUTES*SECONDS)

# 45분간 일하고 10분씩 휴식, 전체 근무시간 480분이면 휴식 시간의 합계는 얼마인가?

WORK = 45
REST = 10
TOTAL_WORK = 480
TOTAL_REST = (TOTAL_WORK/(WORK+REST))*REST
print(TOTAL_REST)

# 숫자를 입력받아 1의 자리까지 버리고 출력
# 예) 3512->3510, 359->350

num = int(input('숫자 입력 : '))
num = float(num//10)*10
print(int(num))

num1 = int(input('숫자 입력 : '))
num2 = float(num1%10)
num3 = num1-num2
print(int(num3))

num4 = int(input('숫자 입력 : '))
num5 = num4 - num4%10
print(num5)

# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수
# 예) 17->14, 21->21

no = int(input('숫자 입력 : '))
no1 = no%7
if no%7==0:
    print(no)
else:
    print(no-no1)

# 자연수를 입력받아 그 숫자보디 직은 최대의 7의 배수
# 예) 17->14, 21->14

no3 = int(input('숫자 입력 : '))
no4 = no3%7
if no3%7==0:
    print(no3-7)
else:
    print(no3-no4)

# 위 문제 다시 풀어볼 것
    # 1-7   0   7*0
    # 8-14 //7  7*1
    #15-21 14   7*2

no5 = int(input('숫자 입력 : '))
no6 = (no5-1)//7