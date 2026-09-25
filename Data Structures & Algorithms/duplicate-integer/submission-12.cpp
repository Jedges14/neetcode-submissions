class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> num(nums.begin(), nums.end());

        return n > num.size();
    }
};