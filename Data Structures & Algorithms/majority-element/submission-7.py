class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = len(nums) // 2

        Ndict = Counter(nums)

        for n in Ndict:
            if Ndict[n] > c:
                return n
