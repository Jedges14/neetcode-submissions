class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        du = {}

        for n in range(len(nums)):
            if nums[n] in du and abs(n - du[nums[n]]) <= k:
                return True
            du[nums[n]] = n

        return False
        