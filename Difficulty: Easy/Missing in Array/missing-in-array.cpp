
class Solution {
  public:
    int missingNum(vector<int>& arr) {
        // Code with Radheshyam (.^.)
        int n=arr.size()+1;
        int sum=0;
        int arrsum=0;
        for(int i=1;i<=n;i++)sum+=i;
        
        for(int i=0;i<arr.size();i++) arrsum+=arr[i];
        
        return sum-arrsum;
    }
};