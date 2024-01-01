#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int main(void){
    int n;
    cin>>n;

    stack<int> s;
    queue<int> q;

    for(int i=0;i<n;i++){
        int num;
        cin>>num;
        q.push(num); 
    }

    int order = 1;

    while(!q.empty()){
        int front = q.front(); //queue 맨 상단
        q.pop();
        
        if(front==order){ //맨 상단이 지금 들어갈 차례라면
            order++;  //넣고
            while(!s.empty() && s.top() == order) { //스택이 비지 않고, 스택 맨 상단이 들어갈 차례라면
                s.pop();
                order++;
            }
        }else{ //아니라면 스택에 보관함.
            s.push(front);
        }
    }

    if(s.empty()){
        cout<<"Nice";
    }else{
        cout<<"Sad";
    }


    return 0;
}
