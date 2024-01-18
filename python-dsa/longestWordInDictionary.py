from typing import List

class Trie:
    def __init__(self, character ,isWord = False) -> None:
        self.isWord = isWord
        self.neighbors = dict()
        self.character = character

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie(character="")
        for w in words:
            current = root;
            for char in w:
                if char not in current.neighbors:
                    current.neighbors[char] = Trie(character=char)
                current = current.neighbors[char]
            current.isWord = True
        
        generated_word = None
        def getWordsFromTrie(node: Trie, curWord):
            nonlocal generated_word
            if not node.isWord:
                return
            if node.isWord:
                word = ((curWord + node.character)[:])
                print(word)
                if (generated_word is None) or (len(generated_word) < len(word)) or (len(word) == len(generated_word) and word < generated_word):
                    generated_word = word

            for neighbor in node.neighbors.values():
                getWordsFromTrie(neighbor, curWord=curWord+node.character)
        for neighbor in root.neighbors.values():
            getWordsFromTrie(neighbor, "");
        return generated_word
        
Solution().longestWord( ["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]
)