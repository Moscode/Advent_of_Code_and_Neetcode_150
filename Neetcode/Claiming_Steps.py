class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        prev_last = 1
        for i in range(n-1):
            temp = prev_last
            prev_last = prev_last + last
            last = temp
        return prev_last
