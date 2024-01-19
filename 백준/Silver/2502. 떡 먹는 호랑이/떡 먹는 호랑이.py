d,k=map(int,input().split())
fib=[1]*(d+1)
for i in range(3,d+1) :
    fib[i]=fib[i-1]+fib[i-2]

for a in range(1,k+1) :
    b=(k-fib[d-2]*a)/fib[d-1]
    if int(b)==b :
        print(a)
        print(int(b))
        break