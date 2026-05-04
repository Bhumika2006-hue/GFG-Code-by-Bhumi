#define ll long long int
class Solution {
  public:
    bool isBinaryPalindrome(int n) {
        ll temp=n;
        ll rev=0;
        while(temp)
        {
            if(temp&1)
            {
                rev|=1;
            }
            temp>>=1;
            if(temp)
            {
                rev<<=1;
            }
        }
        return (n==rev);
    }
};