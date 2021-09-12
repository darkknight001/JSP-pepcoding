n= int(input())
dp = [-1]*(n+1)
dp[0] = 0
dp[1] = 1
def fibRec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    ans = fibRec(n-1) + fibRec(n-2)
    return ans

def fibMemo(n, dp):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n] = fibMemo(n-1, dp) + fibMemo(n-2, dp)
        return dp[n]

def fibTab(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

def fibNormal(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        c = a+b
        a=b
        b=c
    return b
    
# print(fibRec(n))
# print(fibMemo(n, dp))
# print(fibTab(n))
print(fibNormal(n))