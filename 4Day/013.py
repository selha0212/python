# 주민번호를 입력받아 태어난 년도를 4자리로 출력하시오
# 90년대면 1,2 - 2000년대면 3,4

# 1. 주민번호 7번째 자리를 자른다
# 2. 주민번호 앞 2자리를 자른다
# 3. 1번이 1,2면 "19"+2번
#    1번이 3,4면 "20"+2번

jumin = "971213-7012011"
this_year = 2024
if jumin[7:8] == '1' or jumin[7:8] == '2':
    birth_year = int('19' + jumin[0:2])
    age = this_year - birth_year
elif jumin[7:8] == '3' or jumin[7:8] == '4':
    birth_year = int('20' + jumin[0:2])
    age = this_year - birth_year
else : 
    print('잘못입력하셨습니다.')
print(birth_year)
print(age)