class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        mid = len(s) // 2
        a = s[0:mid]
        b = s[mid:len(s)]
        vowels = {'a','e','i','o','u'}
        vowelACount, vowelBCount = 0 , 0;
        for i in range(len(a)):
            if a[i] in vowels:
                vowelACount += 1
            if b[i] in vowels:
                vowelBCount += 1
        return vowelACount == vowelBCount


Solution().halvesAreAlike("textbook")