#include<iostream>
using namespace std;


int ans=INT16_MAX;
int secmin(int arr[],int size){
    for(int i=0 ;i<size;i++){
        if (arr[i]<ans)
        ans=arr[i];
    }
    int second=INT16_MAX;
    for(int i=0;i<size;i++){
        if(ans!=arr[i])
        second=min(second,arr[i]);
    }
    return second;
}
int main(){
    int arr[5]={1,2,3,4,5};
    int size=sizeof(arr)/sizeof(arr[0]);
    int result =secmin(arr,size);
    cout<<"Second min_element is :"<<result<<endl;
    return 0;

}