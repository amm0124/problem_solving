import sys

n=int(input())
C=[0]+list(map(int,sys.stdin.readline().split())) #idx가 방의 번호를 나타냄
dp=[[0,0] for _ in range(n+1)]
dp[1][0]=1
dp[1][1]=C[1]
for room in range(2,n+1) :
    dp[room][0]=dp[room-1][1]+1
    dp[room][1]=max(dp[room-1][0],dp[room-1][1]) + C[room]
    
print(max(dp[n][0], dp[n][1]))