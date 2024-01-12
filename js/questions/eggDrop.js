// https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1
function minMoves(eggs, floors) {
    if (eggs === 1) {
        return floors;
    }
    if (floors === 0 || floors === 1) {
        return floors;
    }
    let ans = Infinity;
    for (let i = 1; i <= floors; i++) {
        // Eggs break from this floor, so try below floors
        const op1 = minMoves(eggs - 1, i - 1);

        // Eggs break from this floor, so try remaining above floors
        const op2 = minMoves(eggs, floors - i);

        // Temp stores minimum moves to find the threshold floor in the worst case
        const temp = 1 + Math.max(op1, op2);

        // We have to minimize the maximum answer
        ans = Math.min(ans, temp);
    }
    return ans;
}

// Example usage
const eggs = 2;
const floors = 10;
const result = minMoves(eggs, floors);
console.log(`Minimum moves needed: ${result}`);
