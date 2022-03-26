import sys

n = int(sys.stdin.readline().replace('\n', ''))
cnt = 0
dp = [0] * n
prev_dp = [0] * n

for _ in range(n):
    tri = list(map(int, sys.stdin.readline().split(' ')))

    if cnt == 0:
        dp[0] = tri[0]

    else:
        for i in range(cnt + 1):
            if i == cnt:
                dp[i] = tri[i] + prev_dp[i - 1]

            elif i - 1 >= 0:
                dp[i] = max(tri[i] + prev_dp[i - 1], tri[i] + prev_dp[i])
            
            elif i == 0:
                dp[i] = tri[i] + prev_dp[i]

    if cnt < n - 1:
        temp = dp
        dp = prev_dp
        prev_dp = temp
    
    cnt += 1

print(max(dp))