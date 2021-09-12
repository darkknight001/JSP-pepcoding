n = int(input())

# # with DP
# def arrangeBuildings(n):
#     dp = [[0]*2 for _ in range(n+1)]
    
#     dp[1][0] = 1
#     dp[1][1] = 1
#     for i in range(2, n+1):
#         dp[i][0] = dp[i-1][1]
#         dp[i][1] = dp[i-1][1]+dp[i-1][0]
    
#     return (dp[n][0]+dp[n][1])**2

# without DP
def arrangeBuildings(n):
    
    lastBuilding = 1
    lastEmpty = 1
    for i in range(n-1):
        prevLastBuilding = lastBuilding #Store no. of ways of 
        lastBuilding = lastEmpty #to hold valid buildings condition
        lastEmpty = prevLastBuilding+lastEmpty
    
    return (lastEmpty+lastBuilding)**2 #As road is on both sides, so ways = ways per side^2

print(arrangeBuildings(n))