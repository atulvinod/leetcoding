/**
 * https://leetcode.com/problems/minimum-cost-to-cut-a-stick/submissions/
 * 
 * solution
 * https://www.youtube.com/watch?v=EVxTO5I0d7w&ab_channel=NeetCodeIO
 */
/**
 * @param {number} n
 * @param {number[]} cuts
 * @return {number}
 */
var minCost = function(n, cuts) {
    let dp =  {}
    function dfs(l, r){
        if ((r -l) == 1){
            return 0;
        }
        let key = `${l},${r}`
        if(dp[key] != undefined){
            return dp[key];
        }
        let result = Number.MAX_SAFE_INTEGER;
        //we try to do every cut in the cuts array,
        //we only have to check if the cut is valid in the current range
        // and get the minimum of all the subsequent valid cuts
        for(const c of cuts){
            if(c > l && c < r){
                result = Math.min(result, (r - l) + dfs(l,c)+ dfs(c,r));
            }
        }
        result = (result == Number.MAX_SAFE_INTEGER ? 0 : result);
        dp[key] = result;
        return result;
    }
    return dfs(0,n)
};

minCost(7,[1,3,4,5])