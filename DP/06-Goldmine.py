import sys
n = int(input())
m = int(input())

mine = [[0]*m for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
for i in range(n):
    mine[i] = list(map(int,input().split()))

def maxGold(r, c, mine):
    if r<0 or r>=len(mine):
        return 0
    
    if c==len(mine[0])-1:
        return mine[r][c]
    
    up  = maxGold(r-1, c+1, mine)
    right = maxGold(r, c+1, mine)
    down = maxGold(r+1, c+1, mine)
    
    curMax = max(up, right, down) + mine[r][c]
    return curMax

def maxGoldMemo(r, c, mine, dp):
    if r<0 or r>=len(mine):
        return 0
    if dp[r][c]!=-1:
        return dp[r][c]
        
    if c==len(mine[0])-1:
        return mine[r][c]
    
    up  = maxGoldMemo(r-1, c+1, mine, dp)
    right = maxGoldMemo(r, c+1, mine, dp)
    down = maxGoldMemo(r+1, c+1, mine, dp)
    
    dp[r][c] = max(up, right, down) + mine[r][c]
    return dp[r][c]

def maxGoldTab(n, m, mine):
    # Storage and meaning
    dp = [[0]*m for _ in range(n)]
    
    # Pre-filling
    for r in range(len(mine)):
        dp[r][m-1] = mine[r][m-1]
    
    for j in range(m-2, -1, -1):
        for i in range(n-1, -1, -1):
            if i+1>=n:
                dp[i][j] = max(dp[i][j+1], dp[i-1][j+1])
            elif i-1<0:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j+1]) 
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j+1], dp[i-1][j+1])
            dp[i][j]+=mine[i][j]
    return max([row[0] for row in dp])
    

# ans = 0
# for i in range(len(mine)):
#     # ans = max(ans, maxGold(i, 0, mine))
#     ans = max(ans, maxGoldMemo(i, 0, mine, dp))
# print(ans)
print(maxGoldTab(n, m , mine))