"""
1. 값 추가 -> input('숫자를 입력해주세요')
2. 리스트 출력
999. 종료 : 감사합니다 -> 종료
"""
# 3번 메뉴를 선택하면 리스트의 합을 출력하시오
# 4번 메뉴를 선택하면 리스트의 평균을 출력하시오

리스트 = []
while True:
    print('1. 값 추가')
    print('2. 리스트 출력')
    print('3. 합계 출력')
    print('4. 평균 출력')
    print('999. 종료')
    select=input("번호 선택:")
    if select=='1':
        num = int(input('숫자 입력:'))
        리스트.append(num)
    elif select=='2':
        print(리스트)
    elif select=='3':
        print(f'입력 값의 합계:{sum(리스트)}')
    elif select=='4':
        print(f'입력 값의 평균:{sum(리스트)/len(리스트)}')
    elif select=='999':
        print("감사합니다.")
        break
    else:
        print('메뉴를 정확하게 입력하세요')