class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # a prefect square is supposed to be the sum of 
        # 1 + 3 + 5 + 7 + 9 ...
        i = 1
        while (num > 0):
            num -= i
            i += 2
        return num == 0