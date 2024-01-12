/**
 * @param {number} n
 * @return {number}
 */
var countVowelStrings = function(n) {
    function solve(numOfChars, n){
        if(n == 1){
            return numOfChars;
        }
        let ways = 0
        for(let i= 0 ; i< numOfChars ; i++){
            ways += solve(numOfChars-i, n-1);
        }
        return ways;
    }
    let result = solve(5, n);
    return result;
};
console.log(countVowelStrings(33))