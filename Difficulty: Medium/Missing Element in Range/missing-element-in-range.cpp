class Solution {
  public:
    vector<int> missinRange(vector<int>& arr, int low, int high) {
        
        vector<int>ans;
        set<int>s;
        for(int i=0;i<arr.size();i++)
        s.insert(arr[i]);
        for(int i=low;i<=high;i++){
            if(s.find(i)==s.end())
            ans.push_back(i);
        }
        return ans;
    }
};