#include<iostream>
using namespace std;

// given an array a[] of size n. Output sum of each
// subarray of the given array.

int main(){

int n;
cin>>n;
int arr[n];

for(int i=0; i<n; i++){
    cin>>arr[i];
}
// int sum[n];
// for(int i=0; i<n;i++){
//     sum[i]=0;
// }
int current=0;

for(int i=0; i<n; i++){
    current=0;
    for(int j=i;j<n; j++){
        // sum[i]+=arr[j];
        current+=arr[j];
        // cout<<sum[i]<<" ";
        cout<<current<<" ";
    }
    cout<<endl;

}
    

    return 0;

}