#Naive Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        while start < len(nums) - 1:
            j = start + 1
            while j < len(nums):
                if nums[start] + nums[j] == target:
                    return [start, j]
                j += 1
            start += 1
        return []


#Optimize Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsMap:
                return [numsMap[complement], i]
            numsMap[nums[i]] = i
        return []