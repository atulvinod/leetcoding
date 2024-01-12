class Solution {
    constructor() {
        this.dp = new Map();
    }

    canPartition(nums) {
        let sum = nums.reduce((acc, num) => acc + num, 0);
        
        // if the total sum cannot be split into 2, then there cannot be a
        // distribution into two sets having equal sum
        if (sum % 2 !== 0) {
            return false;
        }

        let target = sum / 2;
        let result = this.solve(nums, 0, 0, target);
        return result;
    }

    solve(nums, index, currentSum, target) {
        if (index >= nums.length) {
            return currentSum === target;
        }

        if (this.dp.has(currentSum)) {
            return this.dp.get(currentSum);
        }

        // we do the include and exclude method for current number at the index
        // we save the result of the currentSum as it is an overlapping subproblem
        let result =
            this.solve(nums, index + 1, currentSum + nums[index], target) ||
            this.solve(nums, index + 1, currentSum, target);

        this.dp.set(currentSum, result);
        return result;
    }
}

// Example usage:
const solution = new Solution();
const nums = [1, 5, 11, 5];
const canPartitionResult = solution.canPartition(nums);
console.log(canPartitionResult);
