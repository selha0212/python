jumin='961011-1021023'
gender=jumin[7]

# 남자인지 여자인지
if gender=='1':
    print('남자')
else:
    print('여자')

# 둘 중의 하나 if문을 한 줄로 -> 삼항연산자
# 복잡한 삼항 연산은 쓰지말자 -> 스파게티 코드 = 읽기 어려운 코드
print("남자" if gender=='1' else "여자")
# 위 식에서는 'elif 사용불가'

# 외계인 코드 = 관습을 안 지킨 코드
    # 1. currentGender = jumin[7]
    # 2. 네이밍 컨벤션 = 이름을 짓는 파이썬의 관습
    # 3. '1'은 네이밍 컨벤션을 안 지킨 외계인 코드

# gender가 1또는3또는5면 남자, 아니면 여자
print("남자" if gender=='1' or '3' or '5' else "여자")
print("남자" if gender in ('1','3','5') else "여자")

# 주민번호로 나이 출력하기
# 1. 올해의 년도
# 2. 태어난 년도
#    주민번호 앞 2자리를 슬라이싱한다 -> year
#    주민번호 7번째가 '1' 또는 '2'이라면 -> 앞에 '19'+year
#    주민번호 7번째가 '3' 또는 '4'라면 -> 앞에 '20'+year
# 3. 올해의 년도 - int(태어난 년도)

import datetime
this_year = datetime.datetime.now().year # 이건 외우지 않아도 됨 모르면 구글링, GPT 통해 외우기
year = jumin[0:2]
if jumin[7] in ('1','2'):
    year = int('19' + year)
elif jumin[7] in ('3','4'):
    year = int('20' + year)
print(f'{this_year-year}세')
