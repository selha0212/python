lang = 'python'
# slicing
print(lang[0])      #p
print(lang[5])      #n
print('a' in lang)  #false
print('p' in lang)  #true
# 글자는 대소문자 구분

# 뒤에서 slicing (- 붙이면 거꾸로 셈)
print(lang[-1])

string = '123456789'
# 문자열[시작위치:끝위치+1]
print(string[1:3])

# 문자열[시작위치:끝위치+1:간격]
# print(string[1:]) = 숫자 '2'부터 끝까지라는 뜻
print(string[1::5])

# 짝수만 출력
print(string[1::2])
