n, m = map(int, input().split()) # DNA의 수 N, 문자열의 길이 M

data = []
for i in range(n):
    data.append(input()) # DNA 입력

data.sort() # 사전순으로 정렬

dna = ''

for y in range(m):
    value = {'A':0, 'C':0, 'G':0, 'T':0} # ACGT 초기화
    for x in range(n):
        acgt = data[x][y] # n번째 DNA의 m번째 문자 조사
        value[acgt] += 1
    dna += max(value, key=value.get) # m번째 자리에서 가장 빈도 수가 높은 문자열이 저장됨

answer = 0
for x in range(n):
    for y in range(m):
        if dna[y] != data[x][y]:
        # HD : 문자열이 같지 않은 경우 +1
            answer += 1

print(dna) # HD 의 합이 가장 작은 dna
print(answer) # HD 의 합
