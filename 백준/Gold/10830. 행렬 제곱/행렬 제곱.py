import sys
sys.setrecursionlimit(10**8)

def solution(b,matrix):
    if b==1 :
        return matrix
    elif b==2 :
        return matrix_multiplication(matrix, matrix)
    else : #n>=3
        if b&1==0 : #짝수
            result=solution(b//2, matrix)
            return matrix_multiplication(result, result)
        else :
            result=solution(b//2, matrix)
            return matrix_multiplication(matrix_multiplication(result, result), matrix)
        # return solution(n//2, matrix) 
        
#n*n matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    n=len(matrix1)
    answer=[[0 for _ in range(n)] for _ in matrix1]
    
    for row in range(n) :
        for col in range(n) :
            for tmp in range(n) :
                answer[row][col]+=(matrix1[row][tmp]*matrix2[tmp][col])%1000
    
    for row in range(n) :
        for col in range(n) :
            answer[row][col]%=1000

    return answer

n,b=map(int, sys.stdin.readline().split())
matrix=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for row in range(n) :
    for col in range(n) :
        matrix[row][col]%=1000


result=solution(b,matrix)

for row in result:
    print(*row)