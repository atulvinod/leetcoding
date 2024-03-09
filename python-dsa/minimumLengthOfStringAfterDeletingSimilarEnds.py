class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                currentChar = s[l]
                while l < len(s) and s[l] == currentChar:
                    l = l + 1
                while r >= 0 and s[r] == currentChar:
                    r = r - 1
            else:
                break
        return 0 if l > r else r - l + 1


print(Solution().minimumLength(s="aabccabba"))
