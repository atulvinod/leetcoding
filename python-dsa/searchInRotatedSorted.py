class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch( l: int, r : int):
            if  l > r:
                return -1
            
            mid = (r + l) // 2
            midElement = nums[mid]
            if(midElement == target):
                return mid
            '''
                When left is greater than the right, then the whole
                array is unsorted, hence we have to check if the middle element
                is greater than the left element or not and proceed according to where 
                the target may lie
            '''
            if nums[l] > nums[r]:
                if midElement >= nums[l]:
                    if target >= nums[l] and target <= midElement:
                        return bsearch(l, mid-1)
                    else: 
                        return bsearch(mid+1, r)
                else:
                    if target <= nums[r] and target >= midElement:
                        return bsearch(mid +1, r)
                    else:
                        return bsearch(l, mid-1)
            else:
                if target > midElement:
                    return bsearch(mid+1, r)
                else:
                    return bsearch(l, mid-1)
        result = bsearch(0, len(nums)-1)
        return result        