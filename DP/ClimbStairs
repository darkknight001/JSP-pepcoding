n = int(input())


# Recursive
# def climbStairsRec(start, n):
#     if start==n:
#         return 1
    
#     if start>n:
#         return 0
    
#     return climbStairsRec(start+1,n)+climbStairsRec(start+2,n)+climbStairsRec(start+3, n)

# print(climbStairsRec(0,n))

# # Memoization
# def climbStairsMem(src, dest, dp):
#     if src>dest:
#         return 0
#     if src==dest:
#         return 1
    
#     if dp[src]!=-1:
#         return dp[src]
    
#     x = climbStairsMem(src+1, dest, dp)
#     y = climbStairsMem(src+2, dest, dp)
#     z = climbStairsMem(src+3, dest, dp)
    
#     dp[src] = x+y+z
#     return dp[src]

# dp = [-1]*(n+1)
# print(climbStairsMem(0,n, dp))

# Tabulation
def CST(n):
    
    # Storage and meaning
    dp = [0]*(n+1)
    dp[n] = 1
    
    for i in range(n-1, -1, -1):
        for j in range(1,4):
            if i+j<=n:
                dp[i] += dp[i+j]
    return dp[0]
    
print(CST(n))


