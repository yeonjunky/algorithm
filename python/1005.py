import sys

sys.setrecursionlimit(100000)


def get_time(build, estimated_times, dp, current_build):
    time = 0

    for i in build[current_build]:
        if dp[i] == -1:
            dp[i] = get_time(build, estimated_times, dp, i)

        time = max(time, dp[i])

    return estimated_times[current_build - 1] + time


t = int(input())

for _ in range(t):
    build = {}
    n, k = map(int, sys.stdin.readline().split())
    estimated_times = list(map(int, sys.stdin.readline().split()))
    dp = [-1] * (n + 1)

    for i in range(n):
        build[i + 1] = []

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        build[y].append(x)

    w = int(sys.stdin.readline().rstrip())

    print(get_time(build, estimated_times, dp, w))
