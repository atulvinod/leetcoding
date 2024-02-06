from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        config = []
        for i in range(len(strs)):
            current_str_config = Counter(strs[i])
            if len(result) == 0:
                result.append([strs[i]])
                config.append(current_str_config)
            else:
                added = False
                for k in range(len(result)):
                    if len(result[k][-1]) == len(strs[i]):
                        add = True
                        for char, v in config[k].items():
                            if char not in current_str_config or current_str_config[char] != v:
                                add = False
                                break
                        if add:
                            added = True
                            result[k].append(strs[i])
                            break
                    if added:
                        break
                
                if not added:
                    result.append([strs[i]])
                    config.append(current_str_config)
        return result
                            
                            
                                   
Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
                                
                               
                    
        