/**
 * https://leetcode.com/problems/maximum-product-subarray/solutions/
 */
/**
 * We can also do kadane algo with multiplying from l -> r and r -> l and get the max from both the
 * traversals
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let globalMax = nums[0];
    let currentMax = nums[0]
    let currentMin = nums[0];
    for(let i = 1 ; i < nums.length ; i++){
        // if the next number is negative, and the currentMin is also negative,
        // then the overall product will be greater, else we are already,
        // checking for the currentMax validation 
        if(nums[i] < 0){
            [currentMax, currentMin] = [currentMin, currentMax]
        }
        currentMax = Math.max(nums[i], currentMax*nums[i]);
        currentMin = Math.min(nums[i], currentMin*nums[i])
        globalMax = Math.max(globalMax, Math.max(currentMax ,currentMin))
    }

    return globalMax;
};