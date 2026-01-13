
class Solution {
  public:
  int dp[1001][1001];
  int LCS(int i,int j,string &s1, string &s2){
      //base case
      if(i==s1.size() || j==s2.size()) return 0;
      //recursive case
      if(dp[i][j]!=-1) return dp[i][j];
      if(s1[i]==s2[j]) return dp[i][j]= 1+LCS(i+1,j+1,s1,s2);
      else return dp[i][j]= max(LCS(i,j+1,s1,s2),LCS(i+1,j,s1,s2));
  }
  
    int lcs(string &s1, string &s2) {
        memset(dp,-1,sizeof(dp));
        return LCS (0,0,s1,s2);
        
    }
};
