import sys 

n=int(input())
dp=[0 for _ in range(n+1)]
for today in range(1,n+1) : 
    t,p=map(int ,sys.stdin.readline().split())
    future=today+t-1
    max_profit=dp[today-1] #dp[today-1]    
    if future<=n :
        dp[future]=max(dp[future], max_profit + p)
    dp[today]=max(max_profit, dp[today])
print(dp[n])