# 함수, 변수 -> 이름을 가진다 -> 재사용하려고
a = 80
jumsu = 85
# 위 둘 중 아래가 더 좋은 이름 (알아보기 쉬워서)

# 성적합계 = 220점
# sum=220 (△ 별로 좋은 이름이 아님 : 합계가 한 둘이 아니니)
sum_of_all_scores=220

# 구글에 이름 붙이는 방법 다 있음
# 남들한테 보여줄수록 이름 길게 쓰기
# 파이썬은 드물게 대문자를 씀 (대부분 소문자)
# 이름은 알아보기 쉽게, 소문자, _로 만든다

# 키워드(예약어)는 사용할 수 없다
# 파이썬이 사용하는 단어는 사용불가
# ex) True = 10 / if = 100

# 당신의 이름을 변수에 저장하시오
your_name = '이하은'
nai = 22

# 제 이름은 이하은
print("제 이름은",your_name)
# 나이를 1 증가시킨 다음 " 나이는 23 살"이라고 출력
nai = nai+1
print("나이는",nai,"살")

dog_name = '초코'
dog_hobby = '산책'
print("우리집 강아지 이름은",dog_name,"예요")
print(dog_name,"는",dog_hobby,"을 아주 좋아해요")

print("우리집 강아지 이름은 "+dog_name+"예요")
print(dog_name+"는 "+dog_hobby+"을 아주 좋아해요")

monthly_pay=3000000
print("급여 :",monthly_pay)
print("급여 : "+str(monthly_pay))

samsung=78500
user_money=samsung*10
print("총 평가금액 : "+ str(user_money)+"원")