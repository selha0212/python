# 숫자 타입 -> 타입마다 사용할 수 있는 연산, 함수가 다르다
# 산술연산 : = - * / // %
# 10과 3.14 변수
num1, num2 = 10, 3.14
# + - * / 결과 출력 - 한줄로
print(f'합계 : {num1+num2}, {num1-num2}, {num1*num2}, {num1/num2}')

num2 = 3
print(f'몫 : {num1//num2}')
print(f'나머지 : {num1%num2}')

# 함수 : 이름은 가진 기능 -> 재사용하기 위해 이름을 붙인다 
# 내장함수(import 없이 사용가능)
# abs : 절대값 함수
print(abs(-100))
print(abs(100))

# num1의 절대값 출력
print(abs(-5))