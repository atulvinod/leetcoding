class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        prefixEnd = index + len(ch)
        prefix = word[:prefixEnd][::-1]
        suffix = word[prefixEnd:]
        return prefix + suffix


s = Solution()
print(s.reversePrefix(word="abcdefd", ch="ef"))
