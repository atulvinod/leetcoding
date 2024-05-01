class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        def solve(currentStr: str, index: int):
            if index >= len(s):
                return len(currentStr)

            take, dontTake = -float("inf"), -float("inf")

            if currentStr == "" or abs(ord(currentStr[-1]) - ord(s[index])) <= k:
                take = solve(currentStr + s[index], index + 1)

            dontTake = solve(currentStr, index + 1)

            return max(take, dontTake)

        result = solve("", 0)
        return result


s = Solution()
print(s.longestIdealString(s="acfgbd", k=2))
