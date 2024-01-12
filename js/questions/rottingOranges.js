/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
    let queue = []
    let totalOranges = 0;
    let time = 0;
    let markedRotten = {}

    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col] != 0) {
                totalOranges++;
                if (grid[row][col] == 2) {
                    queue.push([row, col]);
                    markedRotten[`${row},${col}`] = true;
                }
            }
        }
    }

    let vectors = [
        [1, 0],
        [0, 1],
        [0, -1],
        [-1, 0],
    ]

    while (queue.length) {
        let queueLength = queue.length;

        // to handle the case when there might not be a possible transformation
        let increment = 0;
        
        while (queueLength--) {
            const [row, col] = queue.shift();
            for (const [x, y] of vectors) {
                let new_row = x + row;
                let new_col = y + col;
                if (new_row >= 0 && new_row < grid.length && new_col >= 0 && new_col < grid[0].length) {
                    if (!markedRotten[`${new_row},${new_col}`] && grid[new_row][new_col] == 1) {
                        queue.push([new_row, new_col])
                        markedRotten[`${new_row},${new_col}`] = true;
                        increment = 1
                    }
                }
            }
        }
        time+=increment;
    }

    const totalRottenOranges = Object.keys(markedRotten).length
    return totalOranges == totalRottenOranges ? time : -1
};

let grid = [[0]]
orangesRotting(grid)