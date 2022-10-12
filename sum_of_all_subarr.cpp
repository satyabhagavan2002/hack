#include <bits/stdc++.h>
using namespace std;

long long subArrSum(int a[], int n){
    int sum = 0;
    for(int i=0; i<n; i++){
        sum += (a[i] * (i+1) * (n-i));
    }
    return sum;
}

int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0; i<n; i++)
        cin>>a[i];
    
    //individual subarrays sum
    // int cur_sum = 0;
    // for(int i=0; i<n; i++){
    //     cur_sum = 0;
    //     for(int j=i; j<n; j++){
    //         cur_sum += a[j];
    //         cout<<cur_sum<<endl;
    //     }
    // }
    cout<<subArrSum(a,n)<<endl;
    return 0;
}