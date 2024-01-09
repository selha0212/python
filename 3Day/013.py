# control : 순서를 바꾼다
# 조건 : 결과가 이럴수도 저럴수도 있다
# jumsu가 짝수인지 홀수인지 출력해라 (2의 배수)
# 10%2 -> 0 / 11%2 -> 1 = 나눠서 나머지가 없는 것이 짝수

jumsu = 75

if jumsu%2==0:
    print('짝수')
else:
    print('홀수')
print('수고하셨습니다')

# jumsu가 3의 배수인지 알고 싶으면 : jumsu%3

# 점수가 90점 이상 우수, 70점 이상 합격, 미만이면 재시험
if jumsu>=90:
    print('우수')
elif jumsu>=70:
    print('합격')
else:
    print('재시험')

# 반복
