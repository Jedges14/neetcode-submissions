class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0;
        int subsum = 0;
        int res = INT_MAX;

        for (int r=0; r<nums.size();r++){
            subsum += nums[r];
            while (subsum >= target){
                res = std::min(res, (r-l+1));
                subsum -= nums[l];
                l++;
            }
        }
        return res == INT_MAX ? 0: res;
    }
};