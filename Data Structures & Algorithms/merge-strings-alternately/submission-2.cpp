class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l = 0;
        int r = 0;
        string res;

        while (l< word1.size() && l<word2.size()){
            res.push_back(word1.at(l));
            res.push_back(word2.at(r));
            l++;
            r++;
        }

        while (l<word1.size()){
            res.push_back(word1.at(l));
            l++;
        }

        while (r<word2.size()){
            res.push_back(word2.at(r));
            r++;
        }

        return res;
    }
};