# 연산
# 산술연산
#   +, -, *, /
# 몫 : //, 나머지 : %
print(18/5)
print(18//5)
print(17%5)

x = 15.82
# x의 소수점 이하를 버리고 출력
print(x//1)

a,b = 19,5
# % 연산 금지. 나머지 4를 출력하시오
#19-(5*(19//5))=4
nmg = a-((a//b)*b)
print(nmg)

y = 453
result = y - y%10
print(result)

result = y//10*10
print(result)
print(y//100*100)

# 숫자를 입력하면 가장 가까운 7의 배수 출력
# 15 -> 21 (21 입력했을 때 21일 나오는 게 정답, 28 나오면 틀림)

# 숫자를 입력하면 그 숫자보다 작은 최대의 짝수
# 7 -> 6