class Solution {
  public:
    int equalSumSpan(vector<int> &a1, vector<int> &a2) {
        int n = a1.size();
        unordered_map<int,int>mp;
        
        int sum1 = 0;
        int sum2 = 0;
        int result = 0;
        
        for(int i=0;i<n;i++){
            sum1 += a1[i];
            sum2 += a2[i];
            
            int diff = sum1 - sum2;
            
            if(diff == 0){
                result = max(result, i+1);
            } else if(mp.count(diff)){
               result = max(result, i - mp[diff]);
            } else {
                mp[diff] = i;
            }
        }
        return result;
        
    }
};