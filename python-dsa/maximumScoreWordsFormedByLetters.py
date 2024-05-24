from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        wordsLength = len(words)
        setSize = pow(2, wordsLength)
        maxScore = 0
        letterCount = dict(Counter(letters))
        wordLetterCounts = list(map(Counter, words))

        for bitMask in range(setSize):
            subset = []
            for bitPos in range(wordsLength):
                if bitMask & (1 << bitPos) != 0:
                    subset.append(bitPos)

            if len(subset) == 0:
                continue

            tempLetterCount = dict(letterCount)
            currentSubsetScore = 0
            validSet = True

            for index in subset:
                wordDict = wordLetterCounts[index]
                currentWordScore = 0
                for char, count in wordDict.items():
                    if char in tempLetterCount and tempLetterCount[char] - count >= 0:
                        tempLetterCount[char] = tempLetterCount[char] - count
                        characterIndex = ord(char) - ord("a")
                        currentWordScore = (
                            currentWordScore + (score[characterIndex]) * count
                        )
                    else:
                        validSet = False
                        break
                if not validSet:
                    break
                currentSubsetScore = currentSubsetScore + currentWordScore

            if validSet:
                maxScore = max(maxScore, currentSubsetScore)

        return maxScore


s = Solution()
s.maxScoreWords(
    words=["dog", "cat", "dad", "good"],
    letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
    score=[
        1,
        0,
        9,
        5,
        0,
        0,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],
)
