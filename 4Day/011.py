# 길이를 입력받아 센티미터 또는 인치로 변환해 출력한다.
# 길이가 양수인 경우 인치로 변환,
# 음수인 경우 센티미터로 변환한다.

TALL = float(input('길이를 입력하세요(센티미터로) -> '))
if TALL>0:
    INCH = TALL * 0.393701
    print(INCH,'inch입니다.')
else:
    print(TALL,'cm입니다.')

길이 = 25
if 길이>0:
    결과 = str(길이/2.54)+'인치'
else:
    결과 = str(길이*2.54)+'cm'
print (결과)

# scope : 변수를 사용할 수 있는 범위, 통용규칙
# 블록이 스코프를 생산하는 언어 : 자바
# 함수가 스코프를 생산하는 언어 : 파이썬