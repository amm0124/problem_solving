n=int(input())
arr=[0]*(n+1)
dp=[0]*(n+1)
for i in range(1,n+1) : 
    t,p=map(int,input().split())
    arr[i]=[t,p]
    
for today in range(1,n+1) :
    future=today+arr[today][0]-1
    max_profit=dp[today-1] #dp[today-1]    
    if future<=n :
        dp[future]=max(dp[future], max_profit + arr[today][1])
    dp[today]=max(max_profit, dp[today])
    
print(dp[n])