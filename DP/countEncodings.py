inputStr = input().replace("\r","")
dp = [-1]*len(inputStr)

# Recursive
def countEncodingsRec(idx, s):
    if idx==len(s):
        return 1
    ans = 0
    if(int(s[idx])>=1 and int(s[idx])<=9):
        ans+=countEncodingsRec(idx+1,s)
    if idx<len(s)-1:
        ch12 = int(s[idx])*10+int(s[idx+1])
        if ch12<=26 and ch12>=10:
            ans+=countEncodingsRec(idx+2,s)
    return ans

# Memoization
def countEncodingsMemo(idx, s, dp):
    if idx==len(s):
        return 1
        
    if dp[idx]!=-1:
        return dp[idx]
        
    ans = 0
    if(int(s[idx])>=1 and int(s[idx])<=9):
        ans+=countEncodingsMemo(idx+1,s, dp)
    if idx<len(s)-1:
        ch12 = int(s[idx])*10+int(s[idx+1])
        if ch12<=26 and ch12>=10:
            ans+=countEncodingsMemo(idx+2,s, dp)
    dp[idx] = ans
    return ans

# Tabulation
def countEncodingsTab(s):
    dp = [0]*(len(s)+1)
    dp[len(s)] = 1
    
    for i in range(len(s)-1,-1,-1):
        ch1 = int(s[i])
        if(ch1>=1 and ch1<=9):
            dp[i] += dp[i+1]
        if i<len(s)-1:
            ch12 = int(s[i])*10+int(s[i+1])
            if ch12<=26 and ch12>=10:
                dp[i] +=dp[i+2]
    return dp[0]
    
# print(countEncodingsRec(0,inputStr))
# print(countEncodingsMemo(0,inputStr, dp))
print(countEncodingsTab(inputStr))