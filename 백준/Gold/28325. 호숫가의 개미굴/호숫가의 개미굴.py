import sys 

def solution(a,b) :
    global n,C,dp
    dp[1][0]=a
    dp[1][1]=b
    
    for room in range(2,n+1) :
        dp[room][0]=dp[room-1][1]+1
        dp[room][1]=max(dp[room-1][0],dp[room-1][1]) + C[room]
    
    if a==0 : #첫 방 선택하지 않음
        return max(dp[n][0],dp[n][1])
    else : #첫 방 선택한 경우
        return dp[n][1]

n=int(input())
C=[0]+list(map(int,sys.stdin.readline().split())) #idx가 방의 번호를 나타냄
dp=[[0,0] for _ in range(n+1)]
print(max(solution(0,C[1]), solution(1,0)))