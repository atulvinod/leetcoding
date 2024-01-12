/**
 * https://leetcode.com/problems/minimum-path-sum/description/
 */
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let dp = {}
    dp[`${grid.length - 1},${grid[0].length - 1}`] = grid[grid.length - 1][grid[0].length - 1];
    let vector = [
        [0, 1],
        [1, 0]
    ]
    for (let i = grid.length - 1; i >= 0; i--) {
        for (let j = grid[0].length - 1; j >= 0; j--) {
            let args = []
            for (let [_x, _y] of vector) {
                if (dp[`${i + _x},${j + _y}`] != null)
                    args.push(dp[`${i + _x},${j + _y}`])
            }
            dp[`${i},${j}`] = grid[i][j] + (args.length ? Math.min(...args) : 0)
        }
    }
    return dp[`0,0`]
};