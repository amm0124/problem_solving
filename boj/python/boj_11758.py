import sys
	def cross_product(p1,p2,p3) :
		x1=p1[0]
		x2=p2[0]
		x3=p3[0]
		y1=p1[1]
		y2=p2[1] 
		y3=p3[1]
		return x1*y2 + x2*y3 + x3*y1 - (x1*y3 + x3*y2 + x2*y1)
	
	p1 =  list(map(int,sys.stdin.readline().split()))
	p2 =  list(map(int,sys.stdin.readline().split()))
	p3 =  list(map(int,sys.stdin.readline().split()))
	
	if cross_product(p1,p2,p3) ==  0 : #일직선
		print(0)
	elif cross_product(p1,p2,p3) <  0 : #시계 방향
		print(-1)
	else : #반시계 방향
		print(1)
