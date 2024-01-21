import sys

n=int(input())
seq=[0]+ list(map(int,sys.stdin.readline().split()))
target=seq[-1]
seq=seq[:-1]
dp=[[0]*21 for _ in range(n+1)]
dp[1][seq[1]]=1

for i in range(2,n) : 
    next_number=seq[i]
    for j in range(21) : #0~20
        if dp[i-1][j]!= 0 : 
            if j+next_number>=0 and j+next_number<=20 :
                dp[i][j+next_number]+=dp[i-1][j]
            if j-next_number>=0 and j-next_number<=20 :
                dp[i][j-next_number]+=dp[i-1][j]

print(dp[n-1][target])