/**
 * https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
 */
let result = 0;
let hashMap = {};

function solve(nums, temp_array, startIndex, currentIndex, currentDiff, indexString) {

    if (temp_array.length >= 3) {
        if (!hashMap[indexString]) {
            console.log(temp_array, " ",indexString);
            result++;
            hashMap[indexString] = true;
        }
    }
    if (currentIndex >= nums.length) {
        return;
    }
    if (temp_array.length == 0) {
        solve(nums, [...temp_array, nums[currentIndex]], currentIndex, currentIndex + 1, currentDiff, indexString + ',' + currentIndex);
    } else if (temp_array.length == 1) {
        solve(nums, [...temp_array, nums[currentIndex]], startIndex, currentIndex + 1, Math.abs(nums[currentIndex] - temp_array[0]), indexString + ',' + currentIndex);
    } else if (Math.abs(temp_array[temp_array.length - 1] - nums[currentIndex]) == currentDiff) {
        solve(nums, [...temp_array, nums[currentIndex]], startIndex, currentIndex + 1, currentDiff, indexString + ',' + currentIndex);
    } else {

    }
    //take

    //dontTake
    solve(nums, [...temp_array], startIndex, currentIndex + 1, currentDiff, indexString);
}


/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function (nums) {
    solve(nums, [], null, 0, Infinity);
    return result;
};

numberOfArithmeticSlices([2,4,6,8,10]);