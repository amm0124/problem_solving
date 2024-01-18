import sys
sys.setrecursionlimit(10**8)
def solution():
    global table,table2,visited,visited2,n
    blue=0 
    red=0 
    green=0
    red_or_green=0
    for i in range(n):
        for j in range(n) :
            if table[i][j]=='B' and visited[i][j]==False:
                dfs(i,j,table[i][j])
                blue+=1 
            elif table[i][j]=='R' and visited[i][j]==False:
                dfs(i,j,table[i][j])
                red+=1
            elif table[i][j]=='G' and visited[i][j]==False:
                dfs(i,j,table[i][j])
                green+=1
    
    #0인 곳만 탐색하자
    for i in range(n):
        for j in range(n) :
            if table[i][j]==0 and visited2[i][j]==False :
                dfs2(i,j) 
                red_or_green+=1
    
    print(red+green+blue, blue+red_or_green)
    
def dfs(pos_x,pos_y,color):
    global table,n,visited
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    if color=='B' : 
        table[pos_x][pos_y]=-1
    else :
        table[pos_x][pos_y]=0
        
    visited[pos_x][pos_y]=True
    for i in range(4) :
        next_x=pos_x+dx[i]
        next_y=pos_y+dy[i]
        if (next_x>=0 and next_x<n) and (next_y>=0 and next_y<n) :
            if table[next_x][next_y]==color and visited[next_x][next_y]==False:
                dfs(next_x, next_y ,color)
                
def dfs2(pos_x,pos_y):
    global table2,n,visited2
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    table[pos_x][pos_y]=-2
    visited2[pos_x][pos_y]=True
    for i in range(4) :
        next_x=pos_x+dx[i]
        next_y=pos_y+dy[i]
        if (next_x>=0 and next_x<n) and (next_y>=0 and next_y<n) :
            if table2[next_x][next_y]==0 and visited2[next_x][next_y]==False:
                dfs2(next_x, next_y)


n=(int)(input())
table=[]
table2=[]
visited=[[False]*n for _ in range(n)]
visited2=[[False]*n for _ in range(n)]
for _ in range(n) :
    inp = sys.stdin.readline().rstrip()
    inp2=[]
    for char in inp :
        inp2.append(char)
    table.append(inp2)
    table2.append(inp2)
    
solution()