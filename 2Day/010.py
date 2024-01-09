# 초를 입력받아 몇분 몇초인지 출력
# 예) 210초라고 입력하면 3분 30초

sec = int(input('시간 : '))
# 3 = 210
minutes = sec//60
# 30 = 210%60
seconds = sec%60
print(f'{minutes}분 {seconds}초')

# 분과 초를 입력하면 초를 출력
# 5분 10초 -> 310초

minut = 5
secon = 10
minsec = (minut*60)+secon
print(minsec,'초')