import sys


def lcs(s1, s2, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                continue

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_len = dp[m][n]

    if lcs_len:
        idx = lcs_len
        lcs_char = [""] * lcs_len
        i = m
        j = n

        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                lcs_char[idx - 1] = s1[i - 1]
                i -=1
                j -=1
                idx -=1

            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1

            else:
                j -= 1

        return (lcs_len, "".join(lcs_char))

    else:
        return (0, "")


first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()

lcs_len, result_str = lcs(first, second, len(first), len(second))

print(lcs_len)

if result_str:
    print(result_str)
