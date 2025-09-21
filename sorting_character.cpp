#include<iostream>
using namespace std;
int main(){
	char arr[100];
	int  n;
	cout<<"Enter the size of array :";
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	for(int i=0;i<n-1;i++){
		char index=i;
		for(int j=i+1;j<n;j++){
			if(arr[j]<arr[index]){
				index=j;
			}
		}
		swap(arr[i],arr[index]);
	}
	cout<<"Sorted Characters :"<<endl;
	for(int i=0;i<ch;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}
