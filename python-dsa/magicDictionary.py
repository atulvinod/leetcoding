from collections import Counter
from typing import List

class MagicDictionary:

    def __init__(self):
        self.dictionary = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            if len(w) not in self.dictionary:
                self.dictionary[len(w)] = []
            self.dictionary[len(w)].append(w)
        

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.dictionary:
            return False
        searchSpace = self.dictionary[len(searchWord)]
        for w in searchSpace:
            i = 0
            while i < len(searchWord) and w[i] == searchWord[i]:
                i += 1
            if i != len(searchWord) and (w[i+1:] == searchWord[i+1:]):
                return 

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

obj = MagicDictionary()
obj.buildDict(["hello","leetcode"])
obj.search("hello")