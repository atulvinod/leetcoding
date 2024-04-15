class Solution:
    def findLatestTime(self, s: str) -> str:
        digits = list(s)
        if digits[4] == "?":
            digits[4] = "9"
        if digits[3] == "?":
            digits[3] = "5"

        if digits[0] == "?" and digits[1] == "?":
            digits[0] = "1"
            digits[1] = "1"
        elif digits[0] == "?":
            digits[0] = "1" if (digits[1] == "0" or digits[1] == "1") else "0"
        elif digits[1] == "?":
            digits[1] = "9" if digits[0] == "0" else "1"

        return "".join(digits)


s = Solution()
print(s.findLatestTime("1?:?4"))
