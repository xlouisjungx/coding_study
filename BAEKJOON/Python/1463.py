import sys

def make_one(n):
    dp = [0] * (n + 1)  # dp[i] : 숫자 i를 1로 만들기 위한 최소 연산 횟수

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1  # 기본적으로 1을 빼는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

# 입력 받기
n = int(sys.stdin.readline().strip())
print(make_one(n))