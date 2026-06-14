class Solution {
public:
    void reverseString(vector<char>& s) {
        if (s.size() == 1){return;}
        int l = 0;
        int r = s.size()-1;

        while(l<r){
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            r--;
            l++;
        }
    }
};