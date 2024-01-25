from typing import List
'''
https://leetcode.com/problems/restore-ip-addresses/
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValidString(string):
            string_len = len(string)
            if string_len > 3 or string_len == 0:
                return False
            
            if string_len > 1:
                if int(string[0]) == 0: 
                    return False
                if string_len == 3:
                    number = int(string)
                    return 100 <= number <= 255
                
            return True
            
        result = []
        def splitString(index, dotCount, currentSegments):
            if index > len(s):
                return
            if dotCount == 1:
                string = s[index:]
                if isValidString(string):
                    currentSegments.append(string)
                    result.append('.'.join(currentSegments))
                    currentSegments.pop()
                return
            
            currentIndex = index
            while (currentIndex < len(s)):
                string = s[index:currentIndex+1]
                if isValidString(string):
                    currentSegments.append(string)
                    splitString(currentIndex+1, dotCount-1, currentSegments)
                    currentSegments.pop()
                if len(string) > 3:
                    break
                currentIndex += 1
        splitString(0,4,[])
        return result
                
                
print(Solution().restoreIpAddresses("25525511135"))