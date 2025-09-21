#include<iostream>
using namespace std;

int main(){
    int arr[3]={1,2,3};
    int i=0;
    int j=2;
    while(i<j){
        swap(arr[i],arr[j]);
        i++;
        j--;
    }
    for(int i=0;i<3;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}