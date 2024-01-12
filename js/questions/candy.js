/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    if(ratings.length <= 1){
        return ratings.length
    }
    let sol = Array.from({length:ratings.length},(_)=>1)
    for(let i = 1; i < ratings.length ; i++){
        if(ratings[i] > ratings[i-1]){
            sol[i] = sol[i-1]+1
        }
    }

    for(let i = ratings.length-1; i > 0 ;i--){
        if(ratings[i-1] > ratings[i]){
            sol[i-1] = Math.max(sol[i]+1, sol[i-1])
        }
    }
    
    return sol.reduce((agg,i)=>agg+i,0)
};