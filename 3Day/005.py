# 비교연산 : 조건 1개
kor,eng = 75,80
print(kor>70, kor>=70)
print(kor<70, kor<=70)
print(kor==70, kor!=70)

# 논리연산
print(not kor>70)
# 조건들을 연결
# and : 하나먄 거짓이면 거짓
# or : 하나만 참이면 참

"""
and
참      참      참
참      거짓    거짓
거짓    참      거짓
거짓    거짓    거짓
"""