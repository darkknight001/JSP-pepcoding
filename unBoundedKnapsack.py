n = int(input())

vals = list(map(int, input().split()))
weights =  list(map(int, input().split()))

cap = int(input())

def unboundedKnapsack(n, vals, weights, cap):
    dp = [0]*(cap+1)
    
    for i in range(1, cap+1):
        for j in range(n):
            if weights[j]<=i:
                remCap = i-weights[j]
                if remCap>=0:
                    remProfit = dp[remCap]
                    totalProfit = vals[j]+remProfit;
                    dp[i] = max(dp[i], totalProfit);
    return dp[cap]

print(unboundedKnapsack(n, vals, weights, cap))