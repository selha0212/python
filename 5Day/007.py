list1 = [1,3,5]

# 10 in list1 : 결과가 참 거짓 (10이 list1에 있니?)

# list1의 원소를 하나씩 꺼내 item에 담는 반복문
for item in list1:
    print(item)

# while 다음에 종료조건이 들어가야 함
index=0
while index<3:
    print(list1[index])
    index+=1

# ctrl + c = 실행 강제 종료 단축키