class Solution {
  public:
    vector<int> findClosestPair(vector<int> &arr1, vector<int> &arr2, int x) {
        int n= arr1.size();
      int m= arr2.size();
      
      int i=0;
      int j=m-1;
      
      int mn = INT_MAX;
      vector<int>ans(2);
      
      while(i<n && j>=0){
          int sum = arr1[i]+arr2[j];
          int diff= abs(sum-x);
          
          if(diff<mn){
              mn=diff;
              ans[0]=arr1[i];
              ans[1]=arr2[j];
          }
          if(sum>x)j--;
          else
          i++;
      }
      return ans;
    }
};