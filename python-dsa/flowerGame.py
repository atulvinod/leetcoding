class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        if n == m:
            return 0
        
        if n < m:
            return self.flowerGame(m, n)
        
        result_arr = []
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i != j and (i + j) % 2 != 0:
                    result_arr.append((i,j))
        
        return len(result_arr)
    
    
Solution().flowerGame(3,2)