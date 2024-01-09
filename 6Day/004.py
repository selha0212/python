# f문자열 : 문자열과 변수를 섞어 내가 원하는 방식을 출력
# replace : 치환
str4 = '010-1111-2222'
# 함수 : 소속 없음
#       소속없는 함수 + 소속있는 메소드
print(len(str4))
# method : 특정 타입 소속 -> 타입은 함수도 가질 수 있다
str4.replace("_",".")
print(str4)

#"971011-2******"
j1 = "971011-2010015"
print(j1.replace(j1[8:],'******'))

str5="     aa aa     "
print(str5.strip())