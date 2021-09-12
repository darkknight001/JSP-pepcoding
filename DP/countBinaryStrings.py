n = int(input())


def cbs(n):
    dp = [[0]*2 for _ in range(n)]
    
    dp[0][0] = 1
    dp[0][1] = 1
    
    for i in range(1,n):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = dp[i-1][0]+dp[i-1][1]
    return dp[n-1][0]+dp[n-1][1]

print(cbs(n))
