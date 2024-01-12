

var fac = function(n){
    if(n<=1){
        return 1;
    }
    return n*fac(n-1)
};

var generatePermutations = function(nums, visited, current, result){
    if(current.length==nums.length){
        result.push(current);
        return;
    }
    for(let i= 0 ; i < nums.length ; i++){
        if(!visited[nums[i]]){
            visited[nums[i]] = true;
            generatePermutations(nums,visited,current+nums[i],result);
            visited[nums[i]] = false;
        }
    }
}

/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    if(n==1){
        return 1;
    }
    let nums = Array.from({length:n},(_,i)=>i+1)
    let current = ''
    let visited = {}
    let factorial = fac(n-1);
    let reducedK = 0;
    let permutationStartRange = []
    for(let i = 1 ; i <= n ; i++){
        if(i == 1){
            permutationStartRange.push(1);
        }else{
             let startRange = permutationStartRange[permutationStartRange.length-1]+factorial
             if(startRange==k){
                current+= (i);
                visited[(i)]= true;
                reducedK = k-startRange
                break
             }else if(startRange>k){
                current+= (i-1);
                visited[(i-1)]= true;
                reducedK = k-permutationStartRange[permutationStartRange.length-1]
                break;
             }else{
                permutationStartRange.push(startRange)
             }
        }
    }
    if(!current.length){
        reducedK = k-permutationStartRange[permutationStartRange.length-1];
        current += nums[nums.length-1];
        visited[current]= true;
    }
    const results = []
    generatePermutations(nums, visited, current, results);
    return results[reducedK]

};

getPermutation(3,6)