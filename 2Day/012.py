# 섭씨를 입력받아 화씨로 출력하시오

celsius = int(input('섭씨 : '))
fahrenheit = celsius*(9/5)+32
print(f'섭씨 {celsius}도는 화씨 {fahrenheit}도')

# 온도와 종류를 입력받으시오
# 예) 온도 : 35 / 종류 : 섭씨
# 종류가 섭씨면 온도를 화씨로 변환, 아니면 섭씨로 변환

cf = input('온도 종류 (섭씨 또는 화씨):')
t = int(input('온도:'))
co = t*(9/5)+32
fo = (t-32)*(5/9)
if cf == '섭씨':
    print(f'종류 : 화씨, 온도 :{co}')
else:
    print(f'종류 : 섭씨, 온도 :{fo}')

# 1. 섭씨면 화씨로, 화씨면 섭씨로 변경하는 프로그램
# 2. 온도 입력 -> 입력 온도가 섭씨? 화씨?
# 3. 섭씨 또는 화씨를 입력받는다 -> 예)kind
# 4. kind가 섭씨면 화씨로 변환

# temp = int(input('온도 입력 : '))
# kind = input('현재 온도 종류(섭씨 또는 화씨)입력 : ')
# if kind == '섭씨':
    #화씨변경
# else:
    #섭씨변경
