n = int(input())
moves = [0]*n

for i in range(n):
    moves[i] = int(input())
  

# # Recursive
# def CSMinMovesR(start, n, moves):
#     if start==n:
#         return 0
    
#     if start>n or moves[start]==0:
#         return -1
    
#     minMoves = 99999
#     for i in range(1,moves[start]+1):
#         currMoves = CSMinMovesR(start+i,n, moves)
#         if currMoves !=-1:
#             # print("current moves at {} : {}".format(start+i, currMoves))
#             minMoves = min(currMoves, minMoves)
#     # print("min moves at {} : {}".format(start, minMoves+1))
#     return minMoves+1

# print(CSMinMovesR(0,n, moves))

# # # Memoization
# def CSMinMovesMemo(start, n, moves, dp):
#     if start==n:
#         return 0
    
#     if start>n or moves[start]==0:
#         return -1
    
#     if dp[start] !=-1:
#         return dp[start]
    
#     minMoves = 99999
#     for i in range(1,moves[start]+1):
#         currMoves = CSMinMovesMemo(start+i,n, moves, dp)
#         if currMoves !=-1:
#             minMoves = min(currMoves, minMoves)
#     dp[start]= minMoves+1
#     return dp[start]

# dp = [-1]*(n+1)
# print(CSMinMovesMemo(0,n, moves, dp))

# Tabulation
def CSMinMovesTab(n, moves):
    
    # Storage and meaning
    dp = [999999]*(n+1)
    dp[n] = 0
    
    for i in range(n-1, -1, -1):
        for j in range(1,moves[i]+1):
            if i+j<=n:
                minMoves =min(dp[i+j], dp[i])
            dp[i] = minMoves
        dp[i] +=1
    return dp[0]
    
print(CSMinMovesTab(n, moves))




