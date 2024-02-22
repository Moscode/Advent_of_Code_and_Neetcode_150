class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurence = dict()
        for char in t:
            occurence[char] = occurence.get(char, 0) + 1

        for char in s:
            occurence[char] = occurence.get(char, 0) - 1
        
        all_zero_values = all(value == 0 for value in occurence.values())

        if all_zero_values:
            return True
        else:
            return False