q = int(input())

for _ in range(q):
    s = list(input())
    n = len(s)
    t = list(input())
    m = len(t)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    print(dp[n][m])
