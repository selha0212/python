# 월급을 입력받아 1년 치 소득세를 제외한 연봉 실수령액을 출력하시오
# 소득세율은 3.3%
# literal = 숫자
TAX_RATE = 0.033
month_pay = int(input('월급 입력 : '))
year_pay = month_pay * 12
sodk = year_pay * TAX_RATE
actual_salary = year_pay - sodk
print(actual_salary,'만 원')