class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r = len(nums)-1
        def bs(nums, l, r, target):
            if l>r:
                return -1

            m = (r+l)//2

            if nums[m] == target:
                return m

            if nums[m] > target:
                return bs(nums, l, m-1, target)

            return bs(nums, m+1, r, target)

        return bs(nums, l, r, target)



        