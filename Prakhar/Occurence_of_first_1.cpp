#include<bits/stdc++.h>
using namespace std;

// actually we have to find **First occurence of 1 in sorted array**
int bs(vector<int> v)
{
    int l=-1,r=v.size();
    int mid;
    while(r-l>1)
    {
        mid = l + (r-l)/2;
        if(v[mid]<1)
        {
            l=mid;
        }
        else
        {
            r=mid;
        }
    }
    return r;
}
int main()
{
    vector<int>v = {0,0,0,0,0,0,1,1,1};
    cout << bs(v);
    return 0;
}
