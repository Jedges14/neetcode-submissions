#include <cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() == 1) return 1;

        int l = 0;
        int r = s.size()-1;

        while (l<r){
            while (l<r and !(isalnum(s[l]))){
                l++;}

            while (l<r and !(isalnum(s[r]))){
                r--;}

            if (tolower(s[l])!= tolower(s[r])){return 0;}

            l++;
            r--;
        }
        return 1;
    }
};
