class Solution {
  public:
    void sortInWave(vector<int>& arr) {
        for(int i=0;i<arr.size()-1;i++){
            int temp = arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=temp;
            i++;
        }
    }
};