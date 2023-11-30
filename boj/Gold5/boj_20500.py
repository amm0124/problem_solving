N=(int)(input())
dp = [[0]*(N+1) for _ in range(3)]
dp[1][1]=1
dp[2][1]=1
for col in range(2,N) :
    for row in range(3) :
        for index in range(3) :
            if row!=index:
                dp[row][col]+=(dp[index][col-1])      
        dp[row][col]=dp[row][col]%1000000007        
print(dp[1][N-1])
