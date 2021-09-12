n = int(input())

arr = [0]*n
for i in range(n):
    arr[i] = int(input())
tar = int(input())

# # Recursion
# def tssRec(idx, arr, tar, curSum):
#     if curSum==tar:
#         return True
    
#     if idx==len(arr):
#         return False
#     s1 = tssRec(idx+1, arr, tar, curSum)
#     s2 = tssRec(idx+1, arr, tar, curSum+arr[idx])
    
#     return s1 or s2

# print("true" if tssRec(0, arr, tar, 0) else "false")

# Memoization
def tssMemo(idx, arr, tar, curSum, dp):
    if curSum==tar:
        return True
    
    if idx==len(arr) or curSum>tar:
        return False
        
    if dp[idx][curSum]!=-1:
        return dp[idx][curSum]
    
    s1 = tssMemo(idx+1, arr, tar, curSum, dp)
    s2 = tssMemo(idx+1, arr, tar, curSum+arr[idx], dp)
    
    dp[idx][0] = s1
    dp[idx][1] = s2
    return (dp[idx][0] or dp[idx][1])
dp= [[-1]*(tar+1) for _ in range(n+1)]
ans = tssMemo(0, arr, tar, 0, dp)
print("true" if ans else "false")
