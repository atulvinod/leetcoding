class Solution:
    def findComplement(self, num: int) -> int:
        binval = bin(num).replace("0b", "")
        result = ""
        for i in binval:
            if i == "1":
                result = result + "0"
            else:
                result = result + "1"
        return int(result, 2)


print(Solution().findComplement(5))
