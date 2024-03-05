import sys
n=int(input())
weights=list(map(int,sys.stdin.readline().split()))
weights.sort()

if weights[0]!=1 :
    print(1)
else : #일단 1은 만들 수 있음.
    prev=1 #1~prev까지는 무조건 만들 수 있음.
    for i in range(1,n) :
        if weights[i]-prev<=1 :
            prev+=weights[i]
        else :
            print(prev+1)
            sys.exit()
    print(sum(weights)+1)