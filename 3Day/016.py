# 숫자를 입력받아 음수면 양수로, 양수면 음수로 바꿔 출력
number = int(input('숫자 입력 : '))
if number<0:
    print(-number)


# 길이를 입력받아 센티미터면 인치로, 인치면 센티미터로 변경
# 1인치 = 2.54센티미터
kind = input('길이(인치/센티미터)종류 : ')
num = int(input('길이 입력 : '))
in_ch = num/2.54
cm_ch = num*2.54

if kind == '인치':
    print(cm_ch,'cm')
elif kind == '센티미터':
    print(in_ch,'인치')
else:
    print('센티미터 또는 인치를 입력하세요')