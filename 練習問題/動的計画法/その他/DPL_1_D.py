from bisect import bisect_left

n = int(input())
a = [int(input()) for _ in range(n)]

dp = [a[0]]
for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        dp[bisect_left(dp, a[i])] = a[i]

print(len(dp))
