class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}

        for i,n in enumerate(nums):
            comp = target - n
            if comp in di:
                return[di[comp], i]

            di[n] = i

        return []        