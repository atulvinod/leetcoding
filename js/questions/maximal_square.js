/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function (matrix) {
    /**
     * Approach: We will find the largest edge and then multiply the edge to find the largest square
     */
    let dp = Array.from({ length: matrix.length }, (_) => Array.from({ length: matrix[0].length }, (_) => 0))
    let max = 0;

    //create the dp array for the leftmost column and the topmost row 
    // save the max edge while processing 
    for (let i = 0; i < matrix.length; i++) {
        dp[i][0] = parseInt(matrix[i][0])
        max = Math.max(max, dp[i][0])
    }
    for (let j = 0; j < matrix[0].length; j++) {
        dp[0][j] = parseInt(matrix[0][j])
        max = Math.max(max, dp[0][j])
    }

    //traverse the matrix 
    for (let i = 1; i < matrix.length; i++) {
        for (let j = 1; j < matrix[0].length; j++) {
            // at every point of the matrix, we will check the edge ending 
            // on the left, top and top-left (diagonal) of the current position
            let left = dp[i-1][j]
            let top = dp[i][j-1]
            let diag = dp[i-1][j-1]

            //if the matrix at current position is one, then there is an edge
            if(matrix[i][j] == 1){
                dp[i][j] = 1;

                // if at the diagonal the matrix was one, 
                // that implies that there was an edge ending at that point
                if(matrix[i-1][j-1] == 1){

                    // if there are equal edges at left, top and diagonal, 
                    // then that implies that the current point will increase the 
                    // size of the overall bigger square.
                    if (top == left && left == diag){
                        dp[i][j] = 1 + top;
                    }else{
                        let min = Math.min(left, top)
                        // if the minimum between the left and top is less than the diagonal,
                        // then we can create atleast create a square whose size is +1 the min value 
                        if(min <= diag){
                            dp[i][j] = 1+min;
                        }else{
                            // else we can create a square of the lowest value
                            dp[i][j] = Math.max(min,1) 
                        } 
                    }
                }   
                max = Math.max(max, dp[i][j]);
            }
        }
    }
    return max * max;
};

let matrix =[["1", "0", "1", "0", "0", "1", "1", "1", "0"],
["1", "1", "1", "0", "0", "0", "0", "0", "1"],
["0", "0", "1", "1", "0", "0", "0", "1", "1"],
["0", "1", "1", "0", "0", "1", "0", "0", "1"],
["1", "1", "0", "1", "1", "0", "0", "1", "0"],
["0", "1", "1", "1", "1", "1", "1", "0", "1"],
["1", "0", "1", "1", "1", "0", "0", "1", "0"],
["1", "1", "1", "0", "1", "0", "0", "0", "1"],
["0", "1", "1", "1", "1", "0", "0", "1", "0"],
["1", "0", "0", "1", "1", "1", "0", "0", "0"]]

maximalSquare(matrix)