from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key=lambda x: (len(x), x))
        matched = None
        for i in range(len(dictionary)-1,-1,-1):
            a, b = 0, 0
            while a < len(s) and b < len(dictionary[i]):
                if s[a] == dictionary[i][b]:
                    a += 1
                    b += 1
                else:
                    a+=1
            if b >= len(dictionary[i]):
                if matched is None or len(matched) == len(dictionary[i]):
                    matched = dictionary[i]
                else:
                    if len(dictionary[i]) < len(matched):
                        return matched
        return matched

Solution().findLongestWord( s = "abce", dictionary = ["abe","abc"])