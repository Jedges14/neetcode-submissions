class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i,v in enumerate(nums):
            com = target - v

            if com in res :
                return [res[com], i]

            else:
                res[v] = i

        return []