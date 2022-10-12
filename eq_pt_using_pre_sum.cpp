#include <bits/stdc++.h>
using namespace std;

bool eqPoint(int a[], int n){
    int sum = 0;
    for(int i=0; i<n; i++) sum += a[i];

    int l_sum = 0;
    for(int i=0; i<n; i++){
        if(l_sum == sum - a[i]) return true;
        l_sum += a[i];
        sum -= a[i];
    }
    return false;
}

int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0; i<n; i++) cin>>a[i];
    cout<<eqPoint(a, n);
    return 0;
}