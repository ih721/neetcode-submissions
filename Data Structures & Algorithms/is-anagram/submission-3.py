#best approach
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            counts[char] = 1 + counts.get(char,0)
        
        for char in t:
            if char not in counts:
                return False
            
            counts[char] -= 1

            if counts[char] < 0:
                return False
        return True


