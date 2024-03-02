class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = []
        for num in nums:
            squared_num = num * num
            squared_nums.append(squared_num)
        return sorted(squared_nums)
        