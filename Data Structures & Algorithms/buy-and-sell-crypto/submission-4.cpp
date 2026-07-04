class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int res = 0;

        for (int r=0; r<prices.size(); r++){
            if (prices[r] > prices[l]){
                int prof = prices[r] - prices[l];
                res = std::max(res, prof);
            }
            else{l=r;}
        }

        return res;
    }
};
