n = int(input())
moves = [0]*n

for i in range(n):
    moves[i] = int(input())
  

# # Recursive
# def CSVR(start, n, moves):
#     if start==n:
#         return 1
    
#     if start>n or moves[start]==0:
#         return 0
    
#     tp = 0
    
#     for i in range(1,moves[start]+1):
#         xi=CSVR(start+i,n, moves)
#         tp+=xi
    
#     return tp

# print(CSVR(0,n, moves))

# # Memoization
# def CSVM(start, n, moves, dp):
#     if start==n:
#         return 1
    
#     if start>n:
#         return 0
    
#     if dp[start]!=-1:
#         return dp[start]
        
#     tp = 0
    
#     for i in range(1,moves[start]+1):
#         xi=CSVM(start+i,n, moves, dp)
#         tp+=xi
    
#     dp[start] = tp
#     return dp[start]

# dp = [-1]*(n+1)
# print(CSVM(0,n, moves, dp))

# Tabulation
def CSVT(n, moves):
    
    # Storage and meaning
    dp = [0]*(n+1)
    dp[n] = 1
    
    for i in range(n-1, -1, -1):
        for j in range(1,moves[i]+1):
            if i+j<=n:
                dp[i] += dp[i+j]
    return dp[0]
    
print(CSVT(n, moves))




