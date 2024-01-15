class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        for i in range(len(nums)):
            index = i - deletions
            if(i+1 < len(nums) and nums[i] == nums[i+1] and index%2 == 0):
                deletions+=1                
        if (len(nums) - deletions) % 2 != 0:
            deletions += 1
        return deletions