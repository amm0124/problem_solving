n=int(input())
dp=[1]*(n+1)
answer=0
for i in range(3,n+1) :
    dp[i]=dp[i-1]+dp[i-2]
    answer+=1
print(dp[n],n-2)