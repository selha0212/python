# 숫자를 2개 입력받아 큰 수와 작은 수를 출력하시오
# 예: 5와 8 중 큰 수는 8, 작은 수는 5입니다.

num1 = int(input('숫자1:'))
num2 = int(input('숫자2:'))
large = max(num1,num2)
small = min(num1,num2)
print(f'{num1}와 {num2} 중 큰 수는 {large}, 작은 수는 {small}입니다.')