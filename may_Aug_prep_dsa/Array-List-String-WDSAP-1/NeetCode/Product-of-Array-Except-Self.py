#BruteForce: time-> O(N^2) and space O(1)
class Solution:
    def productExceptSelf(self, nums):
        answer = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            answer.append(product)
        return answer

#BruteForce: time-> O(N) and space O(N)
class Solution:
    def productExceptSelf(self, nums):
        left_product = [1 for i in range(len(nums))]
        right_product = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        return [left_product[i] * right_product[i] for i in range(len(nums))]

#BruteForce: time-> O(N) and space O(1)
class Solution:
    def productExceptSelf(self, nums):
        answer = [1 for i in range(len(nums))]
        
        prev = 1
        for i in range(len(nums)):
            answer[i] *= prev
            prev *= nums[i]

        next = 1
        for j in range(len(nums)-1, -1, -1):
            answer[j] *= next
            next *= nums[j]
        return answer