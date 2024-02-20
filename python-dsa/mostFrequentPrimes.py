from typing import List

seive = [0]*1000000

for i in range(2, len(seive)):
    if seive[i] == 1:
        continue
    j = 2
    while i*j < len(seive):
        seive[i*j] = 1
        j += 1

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        freq = dict()
        vectors = [
            [1,0],
            [0,1],
            [1,1],
            [-1,1],
            [1,-1],
            [-1,0],
            [0,-1],
            [-1,-1]
        ]

        def process(number :int ,x: int, y: int, vector):
            if number > 10 and seive[number] == 0:
                if number not in freq:
                    freq[number] = 0
                freq[number] += 1
            if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]):
                return
            
            number = number * 10 + mat[x][y]
            process(number ,x+vector[0], y+vector[1], vector)

        for x in range(len(mat)):
            for y in range(len(mat[0])):
                for vector in vectors:
                    process(0, x,y, vector)
        
        maxfreq = 0
        maxnumber = 0
        for n, f in freq.items():
            if f > maxfreq:
                maxfreq = f
                maxnumber = n
            if f == maxfreq:
                maxnumber = max(maxnumber, n)

        return maxnumber
            
Solution().mostFrequentPrime([[1,1],[9,9],[1,1]])
