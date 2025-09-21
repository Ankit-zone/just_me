#include<iostream>
using namespace std;
int main(){
	int arr[100];
	int n;
	cout<<"Enter the size of array :";
	cin>>n;
	
	cout<<"Enter elements :"<<endl;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			if(arr[i]<arr[j]){
				swap(arr[i],arr[j]);
			}
		}
	}	
	cout<<"Sorted Array in Decreasing Order is  :"<<endl;
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}
