/**
 * https://leetcode.com/problems/trapping-rain-water/solutions/3401992/100-detailed-explaination-with-pictures-in-c-java-python-two-pointers/
 */
/**
 * @param {number[]} height
 * @return {number}
 */
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = height[0], rightMax = height[height.length - 1];
        int water = 0;
        /**
         * We maintain two pointers, leftMax and rightMax which indicate
         * the current greatest height at left and vice versa at right
         */
        while (left < right) {

            // we move the smaller max height
            if (leftMax < rightMax) {
                left++;
                // if we find a new max height, update the height
                if (leftMax < height[left]) {
                    leftMax = height[left];
                } else {
                    //it implies that the left height is smaller than
                    // the right, hence left max height will help in determining
                    // the water level
                    water += leftMax - height[left];
                }
            } else {
                right--;
                if (rightMax < height[right]) {
                    rightMax = height[right];
                } else {
                    water += rightMax - height[right];
                }
            }
        }
        return water;
    }
}