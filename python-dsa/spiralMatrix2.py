from typing import List

'''
https://leetcode.com/problems/spiral-matrix-ii/
only diff between this and spiral matrix 1 is that in 1, we have to traverse the 2d matrix
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        numbers = [i for i in range(1,n**2+1)]
        matrix = [ [None]*n for _ in range(n) ]
        top = 0
        left = 0
        right = n -1
        bottom = n - 1
        currentMode = 0;
        currentIndex = 0;
        
        while currentIndex < len(numbers):
            match currentMode:
                # top
                case 0:
                    index = left
                    while index <= right:
                       matrix[top][index]  = numbers[currentIndex]
                       index += 1
                       currentIndex += 1
                    top += 1
                # right
                case 1:
                    index = top
                    while (index <= bottom):
                        matrix[index][right] = numbers[currentIndex]
                        index+= 1
                        currentIndex+=1
                    right -= 1
                # bottom 
                case 2:
                    index = right
                    while index >= left:
                        matrix[bottom][index] = numbers[currentIndex]
                        currentIndex += 1
                        index -= 1
                    bottom -= 1

                #left
                case 3:
                    index = bottom
                    while index >= top:
                        matrix[index][left] = numbers[currentIndex]
                        currentIndex += 1
                        index -= 1
                    left += 1
            
            currentMode = (currentMode+1) % 4
        return matrix
               
               

Solution().generateMatrix(3)    
