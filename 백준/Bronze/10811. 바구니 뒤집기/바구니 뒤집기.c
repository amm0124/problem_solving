#include <stdio.h>

int main(){
    int n,m;
    scanf("%d %d", &n, &m);
    int arr[101];

    for(int i=0; i<101;i++) arr[i]=i;

    for(int i=0;i<m;i++){
        int start, end; //시작과 끝
        scanf("%d %d", &start, &end);
        // 바꾸기
        while(end>start){
            int tmp;
            tmp=arr[start];
            arr[start]=arr[end];
            arr[end]=tmp;
            end--;
            start++;
        }
    }
    
    for(int i=1;i<=n;i++){
        printf("%d ", arr[i]);
    }

    return 0;
}

