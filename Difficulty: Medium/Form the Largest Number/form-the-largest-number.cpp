class Solution {
  public:
          static bool myCompare(string &n1,string &n2){return (n1+n2)>(n2+n1);}

    string findLargest(vector<int> &arr) {
        
        vector<string>numbers;
        for(int i=0;i<arr.size();i++){
            numbers.push_back(to_string(arr[i]));
        }
        sort(numbers.begin(),numbers.end(),myCompare);
        if(numbers[0]=="0") return "0";
        string ans="";
        for(string c : numbers)
        ans.append(c);
        
        return ans;
    }
};