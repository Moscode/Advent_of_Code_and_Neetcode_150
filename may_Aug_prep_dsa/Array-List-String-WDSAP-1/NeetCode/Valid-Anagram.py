#Time -> O(N log N) and space -> O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True

        return False

#Time -> O(N) and space -> O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table = {}

        for char in s:
            if char in hash_table:
                hash_table[char] += 1
            else:
                hash_table[char] = 1
        
        for char in t:
            if char in hash_table:
                hash_table[char] -= 1
            else:
                return False

        for value in hash_table.values():
            if value != 0:
                return False
                
        return True

#Using the knowledge of ASCII time -> O(N) and space -> O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for i in s:
            count[ord(i) - ord('a')] += 1

        for j in t:
            count[ord(j) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
    
        return True