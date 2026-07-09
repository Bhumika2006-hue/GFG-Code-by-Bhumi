class Solution {
  public:
    int countKdivPairs(vector<int>& arr, int k) {
       
        unordered_map<int , int> mp;
        int ans=0;
        for(int i : arr){
            int rem = i%k;
            ans+=mp[rem];
            mp[(k-rem)%k]++;
        }
        return ans;
    }
};