let modulo = Math.pow(10,9)+7;
/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function (n, k, target) {
    if (n <= 0) {
        console.log(n,k,target, " result back");
        return target == 0 ? 1 : 0;
    }
    let ways = 0;
    for (let i = 1; i <= k; i++) {
        ways += numRollsToTarget(n - 1, k, target - i);
    }
    console.log(n,k,target, " result ",(ways)%modulo);

    return (ways)%modulo;
};


console.log(numRollsToTarget(2,6,7))