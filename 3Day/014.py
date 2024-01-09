# 숫자를 입력받아 3의 배수인지 아닌지 출력하시오

number = int(input('숫자 입력 : '))
if number%3==0:
    print('3의 배수입니다')
else:
    print('3의 배수가 아닙니다')


# 점수를 입력받아 90점 이상이면 우수, 70점 이상이면 패스, 미만이면 낙제라고 출력

jumsu = int(input('점수 입력: '))
if jumsu>=90:
    print('우수')
elif jumsu>=70:
    print('패스')
else:
    print('낙제')