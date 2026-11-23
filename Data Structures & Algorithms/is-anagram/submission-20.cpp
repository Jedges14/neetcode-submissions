class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){return false;}

        int c[26] = {0};

        for (int i=0; i<t.size();i++){
            int idx1 = char(t[i]) - 'a';
            int idx2 = char(s[i]) - 'a';

            c[idx1]++;
            c[idx2]--;
        }

      

        for (const auto& a: c){
            if (a !=0) return false;
        }

        return true;
    }
};
