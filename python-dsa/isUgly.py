class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        numbers = [2,3,5]
        for i in numbers:
            while n != 1 and n % i == 0:
                n = n // i
        
        return n == 1
    
Solution().isUgly(14)