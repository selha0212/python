# 주민번호를 입력받아 성별을 출력
jumin = '971012-1035112'
if jumin[7] =='1' or jumin[7] == '3' or jumin[7] == '5':
    print('남자')
else: # elif jumin[7] in ('2','4','6')
    print('여자')

# else:
    print('잘못된 문자입니다.')

# if jumin[7] in ('1','3','5'):
# in은 for문 외에도 쓰이며, 참, 거짓 용도로 사용됨