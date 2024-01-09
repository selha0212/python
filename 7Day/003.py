# 할 일 관리
tno = 1
todos=[
    {'tno':tno, 'title':'할일1', 'reg_day':'2024-01-09','finish':False }
]
# Read : 전체읽기, 1개 읽기
for todo in todos:
    print(todo)

# 할 일 번호를 찾아서 출력
input_tno = int(input('할 일 번호 입력 : '))
for todo in todos:
    if todo['tno']==input_tno:
        print(todo)
        break
    else:
        print('할 일을 찾을 수가 없습니다.')
        찾았니 = True
        break

if 찾았니==False:
    print('할 일을 찾을 수 없습니다')