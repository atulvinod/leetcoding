class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        stringIndex = 0
        patternIndex = 0
        while stringIndex < len(s) and patternIndex < len(p):
            if(p[patternIndex] == '.' and patternIndex + 1 < len(p) and p[patternIndex + 1] == '*'):
                toMatch = s[stringIndex]
                while(stringIndex < len(s) and s[stringIndex] == toMatch ):
                    stringIndex += 1
                patternIndex += 2   
            elif s[stringIndex] == p[patternIndex] or p[patternIndex] == '.':
                stringIndex += 1
                patternIndex +=1
            elif p[patternIndex] == '*':
                if(p[patternIndex - 1] != '.'): 
                    while stringIndex < len(s):
                        if(s[stringIndex] == p[patternIndex - 1]):
                            stringIndex += 1
                        else:
                            break
                patternIndex += 1
            else:
                patternIndex += 1
                        
        result = stringIndex == len(s)
        return result
    
obj = Solution()
obj.isMatch(s =
"aab",
p =
"c*a*b")