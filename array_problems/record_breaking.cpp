#include<iostream>
#include<limits.h>
using namespace std;

int main(){

    int t;
    cin>>t;

    for(int i=1; i<=t;i++){
        int n,rb=0;
        cout<<"enter the n\n";
        cin>>n;
        int arr[n];

        for(int i=0; i<n;i++){
            cin>>arr[i];
        }

        int mx=INT_MIN;
        for(int i=0;i<n;i++){
            mx= max(mx , arr[i]);
            if(i<n-1){
                if(arr[i]>arr[i+1] && arr[i]==mx){
                    rb++;
                }
            }
            else if(arr[i]==mx){
                rb++;
            }
        }

        cout<<i<<":"<<rb<<endl;

    }

    return 0;

}