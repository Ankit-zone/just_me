#include<iostream>
using namespace std;

int main(){
    int arr[5]={1,2,3,4,5};
    int num;
    cout<<"Enter Element for search :";
    cin>>num;
    int index=-1;
    for(int i=0;i<5;i++){
        if (arr[i]==num){
            index+=i;
            break;
        }
    }
    cout<<index;
    return 0;
}