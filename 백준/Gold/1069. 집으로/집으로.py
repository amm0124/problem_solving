import sys,math
x,y,d,t=map(int,sys.stdin.readline().split())
answer=math.sqrt((x**2)+(y**2))
base_distance=answer
count=2
while base_distance-(count)*d>=0:
    count+=1
print(min(answer, t+ abs(base_distance - d) , float(count*t), (count-1)*t+abs(base_distance-(count-1)*d) ))