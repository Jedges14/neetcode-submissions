class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size()>s2.size())return 0;

        unordered_map<char, int> s1c;
        for (const auto &c : s1){
            s1c[c]++;
        }
        string s2sub = s2.substr(0, s1.size());
        unordered_map<char, int> s2c;
        for (const auto &c : s2sub){
            s2c[c]++;
        }

        if (s1c == s2c) return 1;

        for (int r = s1.size(); r<s2.size(); r++){
            s2c[s2[r]]++;
            s2c[s2[r-s1.size()]]--;
            if ( s2c[s2[r-s1.size()]] == 0){s2c.erase(s2[r-s1.size()]);}

            if (s1c == s2c) return 1;
        }
        return 0;
    }
};
