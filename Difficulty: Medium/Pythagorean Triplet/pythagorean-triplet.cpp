class Solution {
  public:
    bool pythagoreanTriplet(vector<int>& arr) {
        unordered_set<int>sq;
        int n=arr.size();
        for(int i=0;i<n;i++) sq.insert(arr[i] * arr[i]);
        
        for(int i=0;i<n;i++){
            int a=arr[i];
            for(int j=0;j<n;j++){
                int b=arr[j];
                
                if(sq.count(a*a + b*b)) return true;
            }
        }
        return false;
    }
};