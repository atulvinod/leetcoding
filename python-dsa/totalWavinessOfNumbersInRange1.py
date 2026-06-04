class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for num in range(num1, num2 + 1):
            strNum = str(num)
            if len(strNum) >= 3:
                for index in range(1, len(strNum) - 1):
                    curNum = int(strNum[index])
                    prevNum = int(strNum[index - 1])
                    nextNum = int(strNum[index + 1])
                    if (curNum > prevNum and curNum > nextNum) or (
                        curNum < prevNum and curNum < nextNum
                    ):
                        waviness += 1

        return waviness


print(Solution().totalWaviness(4848, 4848))
