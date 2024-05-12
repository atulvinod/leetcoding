/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    nums.sort((a,b)=>b-a);
    if(nums.length == 3){
        return nums[0]*nums[1]*nums[2];
    }

    // The number will be either in first 3 indexes, or last three indexes
   return Math.max(nums[0]*nums[1]*nums[2], nums[0]*nums[nums.length-1]*nums[nums.length-2]);
};

maximumProduct([-100,-98,-1,2,3,4])