/**
 * https://leetcode.com/problems/coin-change/description/
 */
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
    if (amount == 0) {
        return 0;
    }
    let map = {};
    const result = _coinChange(coins, amount, map)
    return result == Number.MAX_SAFE_INTEGER ? -1 : result;
};

var _coinChange = function (coins,  amount, map) {
    
    if (amount < 0) {
        return Number.MAX_SAFE_INTEGER;
    }
    if (amount == 0) {
        return 0;
    }
    if(map[amount] != null){
        return map[amount]
    }

    let min = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < coins.length; i++) {
        const res = _coinChange(coins, amount - coins[i],map) + 1
        min = Math.min(min, res);
    }
    map[amount] = min;
    return min;
}