#include <bits/stdc++.h>
using namespace std;

void leftRotByOne(int a[], int n){
    int x = a[0];
    for(int i=1; i<n; i++){
        a[i-1] = a[i];
    }
    a[n-1] = x;

    for(int i=0; i<n; i++) cout<<a[i]<<" ";
    cout<<endl;
}


void Reverse(int a[], int low, int high){
    while(low < high){
        swap(a[high], a[low]);
        low++;
        high--;
    }
}

void leftRotByD(int a[], int n, int d){
    //mySoln --->
    // vector <int> v;
    // for(int i=(d-1); i<n; i++){
    //     v.push_back(a[i]);
    // }
    // for(int i=0; i<(d-1); i++){
    //     v.push_back(a[i]);
    // }
    // for(auto el : v){
    //     cout<<el<<" ";
    // }
    // cout<<endl;




    //naive--->
    // for(int i=0; i<d; i++){
    //     leftRotByOne(a, n);
    // }       




    //most efficient soln--->

    Reverse(a, 0, d-1);
    Reverse(a, d, n-1);
    Reverse(a, 0, n-1);

    for(int i=0; i<n; i++) cout<<a[i]<<" ";
    cout<<endl;

    
}


int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0; i<n; i++)
        cin>>a[i];

    int d;
    cin>>d;

    leftRotByOne(a, n);
    leftRotByD(a, n, d);  
    return 0;
}