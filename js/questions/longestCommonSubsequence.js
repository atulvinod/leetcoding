/**
 * https://leetcode.com/problems/longest-common-subsequence/description/
 * 
 * We take two indexes i and j, for the two texts 
 * if the characters at two indexes are same , then we include 1 with the result as it will be the part
 * of the common subsequence. 
 * if the characters are not the same, then we have three choices, and the max of those choices will be the answer
 * choice 1: increase i+1 and keep j index the same and check for subsequence. which implies keeping j in the seq
 * and checking for other i indexes
 * choice 2: increase j+1 and keep i
 * choice 3: increase i+1 and j+1, hence skipping both of the characters to be included in the sequence.
 */
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    let dp = {}
    function solve(text1, text2, i , j){
        if(dp[`${i},${j}`] != undefined){
            return dp[`${i},${j}`]
        }
        if(i >= text1.length || j >= text2.length){
            return 0
        }

        if(text1[i] == text2[j]){
            let k = 1 + solve(text1, text2,i+1,j+1)
            dp[`${i},${j}`] = k;
            return k;
        }

        let a = solve(text1,text2,i+1,j);
        let b = solve(text1, text2,i,j+1);
        let c = solve(text1,text2, i+1,j+1);
        dp[`${i},${j}`] = Math.max(a, Math.max(b,c))
        return dp[`${i},${j}`];
    }


    const result = solve(text1, text2,0,0);
    return result;
};