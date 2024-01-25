class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = dict()
        def solve(index1, index2):
            if index1 >= len(text1) or index2 >= len(text2):
                return 0
            
            if (index1, index2) in memo:
                return memo[(index1, index2)] 
            
            if text1[index1] == text2[index2]:
                return 1+ solve(index1+1, index2+1)
            
            skipIndex1 = solve(index1+1, index2)
            skipIndex2 = solve(index1, index2+1)
            skipBothIndex = solve(index1+1, index2+1)
            result = max(skipIndex1, skipIndex2, skipBothIndex)
            memo[(index1, index2)] = result 
            return result
        
        result = solve(0,0)
        return result
    
    

print(Solution().longestCommonSubsequence("abc","def"))
            