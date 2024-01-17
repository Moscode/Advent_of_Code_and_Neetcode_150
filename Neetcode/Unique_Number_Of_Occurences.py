class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = dict()
        for num in arr:
            occurence[num] = occurence.get(num, 0) + 1
        values = occurence.values()
        if len(values) == len(set(values)):
            return True
        else:
            return False