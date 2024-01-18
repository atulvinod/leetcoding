'''
https://leetcode.com/problems/can-make-palindrome-from-substring/submissions/
'''
from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        hasharray = [dict()]*len(s)
        init_map = dict()
        init_map[s[0]] = 1
        hasharray[0] = init_map
        result = []
        for i in range(1, len(s)):
            new_countmap = dict(hasharray[i-1])
            hasharray[i] = new_countmap
            new_countmap[s[i]] = 1 if s[i] not in new_countmap else new_countmap[s[i]] + 1
        
        '''
        in this question, we have to check if a substring can be a palindrome, 
        - we can rearrange the characters and we can replace 'k' number of characters to make them palindrome
        - since we can rearrange the characters, then the order given to us is not important, hence we can create a hashmap
        - to make the queries efficient, we can create a hashmap to maintain count of characters upto ith index and to get the 
        hashmap of the given query [start, end] we can take get the hashmap of the substring by creating a hashmap of hashmap[end] - hashmap[start-1]
        values
        - if the count of odd number of characters is one, then it is a palindrome, eg 'baaab'
        - if the count of odd numbers / 2 <= k, then it means we can replace the odd characters to make them even and hence create a palindrome 
        '''
        for [start, end, k] in queries:
            current_map = dict(hasharray[end])
            if start - 1 >= 0:
                for [key, count] in hasharray[start-1].items():
                    current_map[key] = current_map[key] - count 
            oddvaluecount = 0
            for value in current_map.values():
                if value > 0 and value % 2 != 0:
                    oddvaluecount += 1
            if oddvaluecount == 1 or oddvaluecount // 2 <= k:
                result.append(True)
            else:
                result.append(False)
        return result            
             
                    

Solution().canMakePaliQueries( s = "rkzavgdmdgt", queries = [[5,8,0],[7,9,1],[3,6,4],[5,5,1],[8,10,0],[3,9,5],[0,10,10],[6,8,3]])