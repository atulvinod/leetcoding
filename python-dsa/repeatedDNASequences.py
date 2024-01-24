from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        str_map = {}
        left = 0
        right = 9

        while right < len(s):
            cur_str = s[left: right+1] 
            if cur_str in str_map:
                str_map[cur_str] += 1          
            else:
                str_map[cur_str] = 1
            left+=1
            right+=1
            
        result =  [k for (k,v) in str_map.items() if v > 1]
        return result
    
Solution().findRepeatedDnaSequences(s = "AAAAAAAAAAA")