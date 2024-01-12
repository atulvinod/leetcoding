function subSetSums(arr,n){
    const solution = []
    const solve = function(index, arr, currentSum){
        if(index >= arr.length){
            solution.push(currentSum)
            return;
        }

        solve(index+1, arr, currentSum + arr[index])
        solve(index+1, arr, currentSum);
    }
    solve(0, arr, 0)
    return solution;
}

subSetSums([5,2,1])