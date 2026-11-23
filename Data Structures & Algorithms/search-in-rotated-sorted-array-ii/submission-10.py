class Solution:
    def search(self, nums: List[int], target: int) -> bool:
            
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return True

            # Left half is sorted
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
               
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1

            else: l+=1

        return False

                