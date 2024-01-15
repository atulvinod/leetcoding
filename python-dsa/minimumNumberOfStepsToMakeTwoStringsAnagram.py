from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sMap = Counter(s)
        tMap = Counter(t)
        result = 0
        for [key, value] in sMap.items():
            valueInTmap = 0 if key not in tMap else tMap[key]
            if valueInTmap < value:
                result += (value - valueInTmap)
        
        return result

Solution().minSteps("leetcode","practice")