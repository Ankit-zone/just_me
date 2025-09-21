#include<iostream>
using namespace std;


int ans=-1;
int secmax(int arr[],int size){
    for(int i=0 ;i<size;i++){
        if (arr[i]>ans)
        ans=arr[i];
    }
    int second=-1;
    for(int i=0;i<size;i++){
        if(ans!=arr[i])
        second=max(second,arr[i]);
    }
    return second;
}
int main(){
    int arr[5]={1,1,1,1,1};
    int size=sizeof(arr)/sizeof(arr[0]);
    int result =secmax(arr,size);
    cout<<"Seconf max_element is :"<<result<<endl;
    return 0;

}