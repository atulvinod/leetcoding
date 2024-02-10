from typing import List
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        array: List[str] = [a,b,c]
        result = None
        def solve(visited: set, currentString: str):
            nonlocal result
            if len(visited) == 3:
                if result is None or (len(currentString) < len(result) or (len(currentString) == len(result) and currentString < result)):
                    result = currentString[:]
                return
        
            for i in range(len(array)):
                if currentString == "":
                    visited.add(i)
                    solve(visited, array[i])
                    visited.remove(i)
                    continue
                if i in visited:
                    continue
           
                
                # check if can be merged in middle
                fullMatched = False
                for j in range(len(currentString)):
                    if currentString[j:j+len(array[i])] == array[i]:
                        visited.add(i)
                        solve(visited, currentString)
                        visited.remove(i)
                        fullMatched = True
                        break
                
                if fullMatched:
                    continue

                # check if can be appended at start
                visited.add(i)
                startMerged = False
                for j in range(0, len(array[i])):
                    if array[i][j:] == currentString[:len(array[i])-j]:
                        solve(visited, array[i][:j]+currentString)
                        startMerged = True
                        break
                if not startMerged:
                    solve(visited , array[i]+ currentString)
                visited.remove(i)
                
                # check if can be appended to end
                visited.add(i)
                endMerged = False
                for j in range(len(array[i]),0, -1):
                    if array[i][:j] == currentString[-j:]:
                        solve(visited, currentString+array[i][j:])
                        endMerged = True
                        break
                if not endMerged:
                    solve(visited, currentString+array[i])
                visited.remove(i)

        solve(set(),"")
        return result
    
Solution().minimumString(a = "ca", b = "a"
, c = "a")