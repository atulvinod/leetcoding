class Solution:
    def countKeyChanges(self, s: str) -> int:
        lowercased_s = s.lower()
        keyChangeCount  = 0
        for i in range(len(lowercased_s)):
            if i - 1 >= 0:
                if s[i-1] != s[i]:
                    keyChangeCount += 1
        return keyChangeCount