#include<iostream>
using namespace std;
int main(){
	int arr[1000];
	int n;
	cout<<"Enter Size of Array :";
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	for(int i=n-1;i>0;i--){
		int index=i;
		for(int j=0;j<i;j++){
			if(arr[j]>arr[index]){
				index=j;
			}
		}
		swap(arr[i],arr[index]);
	}
	cout<<"Sorted Array :";
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}
