class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if nums[r] > nums[l]:
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid + 1
                else:
                    return mid
            if nums[mid] >= nums[l]:
                if nums[l] < target:
                    r = mid - 1
                elif nums[l] > target:
                    l = mid + 1
                else:
                    return l
            else:
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
        return -1