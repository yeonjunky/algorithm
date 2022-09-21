import sys


def lcs(m, n, s1, s2):
    dp = list([0] * (n + 1) for _ in range(m + 1))

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                continue

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    idx = dp[m][n]
    lcs_char = [""] * idx
    i = m
    j = n

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_char[idx - 1] = s1[i - 1]
            i -= 1
            j -= 1
            idx -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return len(lcs_char)


first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()

print(lcs(len(first), len(second), first, second))
