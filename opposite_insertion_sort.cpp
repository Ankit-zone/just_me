#include<iostream>
using namespace std;
int main(){
	int arr[5]={7,4,2,3,5};
	int n=sizeof(arr)/sizeof(arr[0]);
	for(int i=n-2;i>=0;i--){
		for(int j=i;j<n-1;j++){
			if(arr[j]>arr[j+1]){
				swap(arr[j],arr[j+1]);
			}else{
				break;
			}
		}
	}
	cout<<"Sorted Array is : ";
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}
