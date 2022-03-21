# 동적계획법
# 정수 n을 1,2,3의 합으로 나타내기
# 1 -> 1 1가지
# 2 -> 2, 1+1 -> 2가지
# 3 -> 3, 1+2, 2+1, 1+1+1 -> 4가지
# 4 -> 1+1+1+1 / 2+2 / 1+1+2 3가지 / 1+3 2가지 -> 7가지
# 5 -> 1+1+1+1+1 / 2+2+1 3가지 / 1+1+1+2 4가지 / 1+1+3 3가지 / 2+3 2가지 -> 13가지
# 6 -> 1+1+1+1+1+1 / 1+1+1+1+2 5가지 / 1+1+1+3 4가지 / 1+1+2+2 6가지 / 1+2+3 6가지 / 3+3 / 2+2+2-> 24가지
# 점화식 : dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

T = int(input())
n = [0] * T
for i in range(T):
    n[i] = int(input())

dp = [0] * (max(n)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,max(n)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _,i in enumerate(n):
    print(dp[i])
