#include <bits/stdc++.h>
using namespace std;

//largest element

int largestElOfArr(int arr[], int n){
    int x=0, index=0;
    for(int i=0; i<n; i++){
        if(arr[i] > x){
            x = arr[i];
            index = i;
        }
    }
    return index;
    
}


//second largest element (naive)

int secondLEoA(int arr[], int n){
    int x=0;
    for(int i=0; i<n; i++){
        x = max(x, arr[i]);
    }
    int res=-1, index=0;
    // for(int i=0; i<n; i++){
    //     if(arr[i]>res && arr[i] != x){
    //         res = arr[i];
    //         index = i;
    //     }
    // }
    // return index;
    for(int i=0; i<n; i++){
        if(arr[i] != x){
            if(res == -1)
                res = i;
            else if(arr[i] > arr[res])
                res = i;
        }
    }
    return res;
}

//second largest element (efficient)

int effSecLarEl(int arr[], int n){
    int largest = 0, res = -1;
    for(int i=1; i<n; i++){
        if(arr[i] > arr[largest]){
            largest = i;
            res = largest;
        }
        else if(arr[i] != arr[largest]){
            if(res == -1 || arr[i] > arr[res])
                res = i;
        }
    }
    return res;
}

int main(){
    int n;
    cin>>n;

    int a[n];
    for(int i=0; i<n; i++)
        cin>>a[i];
    
    cout<<"Index of the largest element of the array is: "<<largestElOfArr(a, n)<<endl;
    cout<<"Index of the second largest element of the array is: "<<secondLEoA(a, n)<<endl;
    cout<<"Index of the second largest element of the array is: "<<effSecLarEl(a, n)<<endl;
    return 0;
}