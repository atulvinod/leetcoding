/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function (n) {
    const queenPos = {}
    let solutions = [];
    const vectors = [
        [1, 1],
        [-1, -1],
        [-1, 1],
        [1, -1],
        [0, 1],
        [1, 0],
        [-1, 0],
        [0, -1]
    ]

    function traverse(vector, x, y) {
        if (queenPos[x + ',' + y]) {
            return false;
        }
        if (x < 1 || x > n || y < 1 || y > n) {
            return true;
        }
        return traverse(vector, vector[0] + x, vector[1] + y)
    }

    function checkValidPosition(index, currentRow , col){
        if(index>=vectors.length){
            return true;
        }
        let result = traverse(vectors[index], currentRow,col)
        if(!result){
            return false;
        }
        return checkValidPosition(index+1,currentRow,col)
    }

    function solve(currentRow, n) {
        if (currentRow > n) {
            const solution = []
            for (let row = 0; row < n; row++) {
                let solRow = ''
                for (let col = 0; col < n; col++) {
                    if (queenPos[(row + 1) + ',' + (col + 1)]) {
                        solRow += 'Q'
                    } else {
                        solRow += '.'
                    }
                }
                solution.push(solRow)
            }
            solutions.push(solution)
            return;
        }
        for (let col = 1; col <= n; col++) {
            let isValidPosition =  checkValidPosition(0, currentRow, col)

            if (isValidPosition) {
                queenPos[currentRow + ',' + col] = true;
                solve(currentRow + 1, n);
                queenPos[currentRow + ',' + col] = false;
            }

        }
    }
    solve(1, n)
    return solutions;
};

solveNQueens(4)


