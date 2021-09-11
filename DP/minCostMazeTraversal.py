import sys
n = int(input())
m = int(input())

maze = [[0]*m for _ in range(n)]

for i in range(n):
    maze[i] = list(map(int,input().split()))


# # Recursion
# def minCostTraversal(row, col, maze):
    
    
#     if(row == len(maze)-1 and col==len(maze[0])-1):
#         return maze[row][col]
    
#     if row == len(maze) or col==len(maze[0]):
#         return 999999
    
#     # minCost = sys.maxsize
    
#     hWay = minCostTraversal(row, col+1, maze)
#     vWay = minCostTraversal(row+1, col, maze)
    
#     minCost = min(hWay, vWay)
#     minCost+= maze[row][col]
    
#     return minCost
    
# print(minCostTraversal(0,0,maze))  


# # Memoization
# def minCostTraversalMemo(row, col, maze, dp):
    
    
#     if(row == len(maze)-1 and col==len(maze[0])-1):
#         return maze[row][col]
    
#     if row == len(maze) or col==len(maze[0]):
#         return 999999
    
#     # minCost = sys.maxsize
#     if dp[row][col]!=-1:
#         return dp[row][col]
#     hWay = minCostTraversalMemo(row, col+1, maze, dp)
#     vWay = minCostTraversalMemo(row+1, col, maze, dp)
    
#     minCost = min(hWay, vWay)
#     dp[row][col]= minCost+ maze[row][col]
    
#     return dp[row][col]

# dp = [[-1]*(m+1) for _ in range(n+1)]
    
# print(minCostTraversalMemo(0,0,maze, dp))  

# Tabulation
def minCostTraversalTab(n, m, maze):
    # storage and meaning
    dp = [[-1]*(m+1) for _ in range(n+1)]
    
    # Pre-filling
    dp[len(maze)] = [sys.maxsize]*(m+1)
    for i in range(n+1):
        dp[i][m] = sys.maxsize
        
    dp[n-1][m-1] = maze[n-1][m-1]
    
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i==n-1 and j==m-1:
                continue
            dp[i][j] = min(dp[i+1][j], dp[i][j+1])
            dp[i][j]+=maze[i][j]
            
    return dp[0][0]
print(minCostTraversalTab(n,m,maze))  



