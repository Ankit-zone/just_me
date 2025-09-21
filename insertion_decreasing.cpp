//Use Insertion Sort Algorithm to sort the array of integers in decreasing order.
#include<iostream>
using namespace std;
int main(){
	int arr[100]={7,4,2,3,5};
	for(int i=1;i<=4;i++){
		for(int j=i;j>0;j--){
			if(arr[j]>arr[j-1]){
				swap(arr[j],arr[j-1]);
			}else{
				break;
			}
		}
	}
	cout<<"Sorted Array in Decreasing Order:"<<endl;
	for(int i=0;i<5;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}
