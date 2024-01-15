#greedy : 정렬
import sys

N,K,T = map(int ,sys.stdin.readline().split()) # N: 바구니, K : 터지는 , T : 최대 횟수
nadori = list(map(int, sys.stdin.readline().split())) #nadori < K
nadori.sort()
nadori.reverse()
nadori_sum=sum(nadori)

if nadori_sum==0 : 
    print("YES")
else : 
    if nadori_sum%K==0: #일단 되기는 함.
        #투포인터 
        max_index=0 # 제일 큰 인덱스 가리키는
        min_index=N-1 #제일 작은 인덱스 가리키는
        
        while max_index<min_index : #max_index>=min_index 경우 탈출함 , 즉 교차되거나 같아지는 경우
            #print(nadori)
            #TASK 처리를 잘 해줘야 풀기 가능
            min_index_nadori=nadori[min_index]
            max_index_nadori=nadori[max_index]
            need_nadori = K-max_index_nadori #max_index에 넣어야 할 나도리의 수
            
            #필요한 나도리의 수가 min_index 나도리보다 큰 경우
            #이 경우, 최대한 채우고, min_index를 한 칸 감소시킨다.  
            if need_nadori > min_index_nadori : 
                #T를 신경 안써도 되는 경우임 구현 해야함
                if T>min_index_nadori : 
                    nadori[max_index]+=min_index_nadori #기존 값보다 더함
                    nadori[min_index] = 0
                    min_index-=1
                    T-=min_index_nadori
                #T=<min_index_nadori, 
                #나도리가 부족한데, T까지 부족하므로 NO! 
                else :
                    print("NO")
                    exit()
            
            #필요한 나도리의 수 == 옮길 나도리의 수
            elif need_nadori == min_index_nadori :
                #T가 충분하다면 그냥 옮기기
                if T>=min_index_nadori :
                    nadori[max_index] = K
                    nadori[min_index] = 0
                    max_index+=1
                    min_index-=1
                    T-=min_index_nadori
                    if T==0 : #T==0
                        if max_index > min_index :
                            print("YES")
                            exit()
                    else:  #T>0
                        continue
                #T가 진짜 부족한 경우
                else :
                    print("NO")
                    exit()
                    
            #need_nadori < min_index_nadori . . 
            #필요한 나도리의 수 < 옮기기 가능한 나도리의 수
            else :
                #그냥 옮김 -> 필요한 나도리의 수 만큼 옮기자
                if T>need_nadori :
                    nadori[max_index] = K
                    nadori[min_index] -=need_nadori
                    max_index+=1
                    T-=need_nadori
                # T<=need_nadori 
                else:  
                    print("NO")
                    exit()       
        print("YES")
    else :
        print("NO")

