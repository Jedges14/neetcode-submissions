class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        while(i<n){
            int j = i+1;
            while(j<n){
                if(nums[i]==nums[j]){
                    return true;
                }
                j++;
            }
            i++;
        }
        return false;
    }
};