# 반지름을 입력받아 원의 면적(파이*반지름*반지름)을 출력
ban = int(input('반지름 : '))
PI = 3.14
one = PI*ban*ban

# 반지름을 입력받아 원 둘레(2*파이*반지름)을 출력
two_re = 2*PI*ban
print(f'원의 반지름 : {ban}, 원의 면적 : {one}, 원의 둘레 : {two_re}')