#include<iostream>
using namespace std;
int main(){
	int arr[5]={1,3,5,6,9};
	int start=0;
	int end=4;
	int mid,target=6;
	while(start<=end){
		mid=(start + end )/2;
		if(arr[mid]==target){
			cout<<"Found At Index :"<<mid<<endl;
			break;
		}
		else if(arr[mid]<target){
			start=mid+1;
		}
		else{
			end=mid-1;
		} 
		
	}
	return 0;
}
