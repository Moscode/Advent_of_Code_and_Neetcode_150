class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value_counts = dict()
        for value in nums:
            if value_counts.get(value, 0) + 1 > 1:
                return True
            value_counts[value] = value_counts.get(value, 0) + 1
        return False

