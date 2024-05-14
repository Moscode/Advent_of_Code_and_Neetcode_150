#Brute Force Approach - time: O(n) and space: O(1)

# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        if n == 1:
            return arr[0]
        for i in range(n):
            if i > 0 and i < n - 1:
                left_check = arr[i - 1]
                right_check = arr[i + 1]
                if arr[i] >= left_check and arr[i] >= right_check:
                    return i
            elif i == 0:
                right_check = arr[i + 1]
                if arr[i] >= right_check:
                    return i
            else:
                left_check = arr[i - 1]
                if arr[i] >= left_check:
                    return i
                    
        return -1

#Optimal Approach using Binary Search - time: O(logn) and space: O(1)
#Binary Search on nonsorted array although we are certain about an answer in the increasing side of the mid point
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        l, r = 0, len(arr) - 1
        while l <= r:
            midpt = l + (r - l)//2
            if midpt > 0 and arr[midpt] < arr[midpt - 1]:
                r = midpt - 1
            elif midpt < len(arr) - 1 and arr[midpt] < arr[midpt + 1]:
                l = midpt + 1
            else:
                return midpt