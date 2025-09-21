#include<iostream>
using namespace std;

int main(){
	char arr[26];
	int n;
	cout<<"Enter Size of Array:";
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			if(arr[i]>arr[j]){
				swap(arr[i],arr[j]);
			}
		}
	}
	cout<<"Sorted Character array :";
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}
