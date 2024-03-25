import sys

n=int(input())
tiles=list(map(int, sys.stdin.readline().split()))  
answer=0
index_diff=dict()
for i in range(n) :
    index_diff[tiles[i]]=i
memo=dict()

for row in range(n) :
    for col in range(row+1,n) :
        s=tiles[row]
        e=tiles[col]
        diff=e-s # 간격
        depth, tmp = 2, s+e
        while True :
            if e+diff not in index_diff :
                break
            else :
                e+=diff
                tmp+=e
                depth+=1      
        if depth>=3 : 
            if diff not in memo :
                memo[diff]=tmp
            else :
                memo[diff]=max(memo[diff],tmp)
            answer=max(answer,tmp)
           
print(answer)