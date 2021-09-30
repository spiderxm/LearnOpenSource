#include<iostream>
using namespace std;

int main(){

    cout<<"enter total test cases \n";

    int T;
    cin>>T;


    for(int i=0; i<T; i++){
        int n; 
        cout<<"enter n \n";
        cin>>n;
        int arr[n];
        cout<<"now, enter ai values\n";

        for(int i=0;i<n;i++){
            cin>>arr[i];
        }

        int pd= arr[1]-arr[0];
        int ans=2; 
        int current=2;
        int j=2;
        while(j<n){
            if(pd==arr[j]-arr[j-1]){
                current++;
            }
            else{
                pd = arr[j]-arr[j-1];
                 current=2;
            }
            ans= max( ans, current);
            j++;
        }
        cout<<T<<":"<<ans<<endl;
    }

    return 0;

}