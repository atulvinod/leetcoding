class Solution {
    //Function to find the minimum number of platforms required at the
    //railway station such that no train waits.
    findPlatform(arr, dep, n) {
        arr.sort((a, b) => a - b)
        dep.sort((a, b) => a - b)
        let max = 1;
        let cur = 0
        let i = 0;
        let j = 0
        while (i < arr.length) {
            if (arr[i] <= dep[j]) {
                max = Math.max(++cur, max)
                i++;
            } else {
                cur--;
                j++;
            }
        }
        return max;
    }
}

new Solution().findPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000])