/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    const stack = []
    const map = {}
    
    for(let i = nums2.length-1 ; i >= 0 ; i --){
        while(stack.length && stack[stack.length-1] <= nums2[i]){
            stack.pop()
        }

        if(!stack.length){
            map[nums2[i]] = -1;
        }else{
            map[nums2[i]] = stack[stack.length-1]
        }
        stack.push(nums2[i])
    }

    let result = []
    for(let i = 0 ; i < nums1.length ; i++){
        result.push(map[nums1[i]])
    }
    return result
};


nextGreaterElement([4,1,2],[1,3,4,2])