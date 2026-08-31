class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){return false;}

        unordered_map<char, int> s1;
        // unordered_map<char, int> t1;

        for (int i=0; i<s.size();i++){
            s1[s[i]] ++;
            s1[t[i]] --;
        }

        for (const auto& v: s1){
            if (v.second != 0) return false;
        }

        return true;
    }
};
