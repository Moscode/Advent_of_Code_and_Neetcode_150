class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid_point = (l + r) // 2
            if nums[mid_point] < target:
                l = mid_point + 1
            elif nums[mid_point] > target:
                r = mid_point - 1
            else:
                return mid_point
        return -1