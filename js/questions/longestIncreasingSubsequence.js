/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {

    /**
     * We take an approach of take and dont take.
     * we can skip the element, and take the element if the previous element
     * smaller than the current element and take the max of both of these function calls
     */
    function solve(nums, i, prev) {
        if (i >= nums.length) {
            return 0;
        }

        let take = 0, dontTake = solve(nums, i + 1, prev);
        if (nums[i] > prev) take = 1 + solve(nums, i + 1, nums[i])
        return Math.max(take, dontTake)
    }
    return solve(nums, 0, Number.MIN_SAFE_INTEGER);
};

//memoized
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
    /**
    * We memoized the earlier solution using dp map
    */
    let dp = {}
    function solve(nums, i, prev) {
        if (i >= nums.length) {
            return 0;
        }
        if (dp[`${i},${prev + 1}`] != undefined) {
            return dp[`${i},${prev + 1}`]
        }
        let take = 0, dontTake = solve(nums, i + 1, prev);
        if (prev == -1 || nums[i] > nums[prev]) take = 1 + solve(nums, i + 1, i)
        dp[`${i},${prev + 1}`] = Math.max(take, dontTake)
        return dp[`${i},${prev + 1}`]
    }
    return solve(nums, 0, -1);

};

//tabulated
/**
 * We can solve it iteratively as well. Here, we use dp array where dp[i] denotes the LIS ending at index i. 
 * We can always pick a single element and hence all dp[i] will be initialized to 1.

For each element nums[i], if there's an smaller element nums[j] before it, the result 
will be maximum of current LIS length ending at i: dp[i], and LIS ending at that j + 1: dp[j] + 1. 
+1 because we are including the current element and extending the LIS ending at j.

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int ans = 1, n = size(nums);
        vector<int> dp(n, 1);
        for(int i = 0; i < n; i++) 
            for(int j = 0; j < i; j++) 
                if(nums[i] > nums[j]) 
                    dp[i] = max(dp[i], dp[j] + 1), ans = max(ans, dp[i]);
        return ans;
    }
};
Time Complexity : O(N2)
Space Complexity : O(N)


 */


lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]);