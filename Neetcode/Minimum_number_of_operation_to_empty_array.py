class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def min_steps_to_one(number):
            steps = 0
            while number % 3 != 0:
                number -= 2
                steps += 1
            steps += number // 3

            return steps

        res = {}
        solution = 0
        for num in nums:
            res[num] = res.get(num, 0) + 1

        for val in res.values():
            if val == 1:
                return -1
            else:
                solution += min_steps_to_one(val)
        return solution