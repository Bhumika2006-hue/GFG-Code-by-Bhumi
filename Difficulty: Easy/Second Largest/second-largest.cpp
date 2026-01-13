// User function template for C++
class Solution {
  public:
    // Function returns the second
    // largest elements
    int getSecondLargest(vector<int> &arr) {
        // Code Here
        //sort(arr.begin(),arr.end());
        int largest=arr[0];
        int seclargest=INT_MIN;
        int n=arr.size();
        for(int i=1;i<n;i++){
            if(arr[i]>largest){
                seclargest=largest;
                largest=arr[i];
            }
            else if(arr[i]<largest && arr[i]>seclargest){
                seclargest=arr[i];
            }
        }
        if(seclargest!=INT_MIN) return seclargest;
        return -1;
    }
};