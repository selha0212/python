# 타입, 변수, 산술연산 (+,-,*,  /,//,  %)
# 조건문(if문)
# a = 1
# if a>5 :
#    print('5보다 큽니다')
#    print('if가 참이면 동작') 들여 쓴 경우 조건이 참일 때 동작
# print('if와 관계없다') 그냥 쓴 경우 if와 관계없이 동작

money = 5000
if money>=4500:
    print('떡볶이를 먹어요')
    print('행복합니다')
else:
    print('집에 가서 물이나 먹읍시다')
print('집에 왔어요')

# 점수를 입력받아 70점 이상이면 합격, 아니면 불합격이라고 출력
# 17라인 출력이 끝나면 "수고하셨습니다"라고 출력

wjatn = int(input('점수 : '))
if wjatn>=70:
    print('합격')
else:
    print('불합격')
print('수고하셨습니다')