class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True        
        mask = 1
        while mask <= n:
            if n ^ mask == 0:
                return True
            mask = mask << 1
        
        return False
    

Solution().isPowerOfTwo(16)
    
