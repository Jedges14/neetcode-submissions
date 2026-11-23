class Solution:
    def search(self, nums: List[int], target: int) -> bool:
            
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return True

            # Handle duplicates (remove if array elements are guaranteed unique)
            if nums[l] == nums[mid] == nums[h]:
                l += 1
                h -= 1
                continue

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
                # Right half is sorted
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1

        return False

                