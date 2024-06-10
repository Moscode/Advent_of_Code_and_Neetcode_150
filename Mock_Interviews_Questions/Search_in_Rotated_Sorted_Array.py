class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            midpt = left + (right - left) // 2

            if nums[midpt] == target:
                return midpt
            
            if  nums[left] <= nums[midpt]:
                if nums[left] <= target < nums[midpt]:
                    right = midpt - 1
                else:
                    left = midpt + 1
            else:
                if nums[midpt] < target <= nums[right]:
                    left = midpt + 1
                else:
                    right = midpt - 1
        return -1