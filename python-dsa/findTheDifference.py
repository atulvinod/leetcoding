from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_map = Counter(t)
        for i in range(len(s)):
            t_map[s[i]] -= 1
        
        for [key, value] in t_map.items():
            if value == 0:
                return key
            
        return ""
    

Solution().findTheDifference(s = "abcd", t = "abcde")