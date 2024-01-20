'''
#GOOD #IMPORTANT Question
https://leetcode.com/problems/sum-of-subarray-minimums/description/?envType=daily-question&envId=2024-01-20

We use monotonic stack to calculate the previous smaller element and next smaller element

for a value at ith element, it will be smaller for arrays between smaller value at indexes lower than ith element
and higher at ith element

we calculate the number of elements between these elements 

'''

from typing import List
modulo = 10**9+7
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        previous_smaller_element = [-1]*len(arr)
        next_smaller_element = [len(arr)]*len(arr)
        stack = []
        
        # to calculate the previous smaller element 
        for i in range(len(arr)):
            while len(stack) != 0 and  arr[i] < arr[stack[-1]]:
                stack.pop()
            if len(stack) != 0:
                previous_smaller_element[i] = stack[-1] 
            stack.append(i)
        
        stack.clear()
        # to calculate the next smaller element
        for i in range(len(arr)):
            while len(stack) != 0 and arr[i] < arr[stack[-1]]:
                top_element_index = stack[-1]
                next_smaller_element[top_element_index] = i
                stack.pop()
            stack.append(i)
        
        total_sum = 0
        for i in range(len(arr)):
            left = previous_smaller_element[i]
            right = next_smaller_element[i]
            left_count = i - left
            right_count = right - i
            total = arr[i] * left_count * right_count
            total_sum = (total + total_sum)%modulo
        return (total_sum) % modulo 
    
Solution().sumSubarrayMins([11,81,94,43,3])
            