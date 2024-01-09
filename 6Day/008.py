numbers=[]
while True:
    print('==========숫자 CRUD==========')
    print('1.추가 2.출력 3.합계 4.값으로 삭제 999.종료')
    select=input('메뉴선택 : ')
    if select=='1':
        num=int(input('숫자추가:'))
        numbers.append(num)
    elif select=='2':
        for number in numbers:
            print(number)
    elif select=='3':
        print(f'합계:{sum(numbers)}')
    elif select=='4':
        val=int(input('삭제할 값 : '))
        if val in numbers:
            numbers.remove(val)
    elif select=='999':
        print('감사합니다.')
        break
