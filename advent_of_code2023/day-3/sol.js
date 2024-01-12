const puzzle_input = require('./puzzle_input');

const test = [
    "467..114.."
    , "...*......"
    , "..35..633."
    , "......#..."
    , "617*......"
    , ".....+.58."
    , "..592....."
    , "......755."
    , "...$.*...."
    , ".664.598.."
]

let vector = [
    [-1,0],
    [-1,1],
    [0,1],
    [1,1],
    [1,0],
    [1,-1],
    [0,-1],
    [-1,-1]
]

function isDigit(char) {
    return char >= '0' && char <= '9'
}

function getNumber(puzzle, row, col) {
    let number = ''
    //traverse to leftmost of the number
    while (col - 1 >= 0 && isDigit(puzzle[row][col - 1])) {
        col -= 1;
    }

    //traverse to the right to get the full number
    while (col < puzzle[0].length && isDigit(puzzle[row][col])) {
        number += puzzle[row][col];
        col += 1
    }

    //parse and return the number

    return {num: Number(number), key:`${row},${col}`}
}

const isValidBound = (puzzle, row, col) => row >= 0 && row < puzzle.length && col >= 0 && col < puzzle[0].length

function solve1part(puzzle) {
 
    let sum = 0
    for (let row = 0; row < puzzle.length; row++) {
        for (let col = 0; col < puzzle[0].length; col++) {
            if(isDigit(puzzle[row][col]) || puzzle[row][col] == '.'){
                continue;
            }
            let nums_found = {}
            for (const [_x, _y] of vector) {
                let nrow = _x + row;
                let ncol = _y + col;
                let is_valid = isValidBound(puzzle, row, col);
                if (is_valid && isDigit(puzzle[nrow][ncol])) {
                    let {num, key} = getNumber(puzzle, nrow, ncol);
                    nums_found[key] = num
                }
            }
            sum += Object.values(nums_found).reduce((agg,v)=>agg+v,0)
        }
    }


    console.log(sum)
}

function solve2part(puzzle){
    let sum = 0
    for (let row = 0; row < puzzle.length; row++) {
        for (let col = 0; col < puzzle[0].length; col++) {
            if(isDigit(puzzle[row][col]) || puzzle[row][col] != '*'){
                continue;
            }
            let nums_found = {}
            for (const [_x, _y] of vector) {
                let nrow = _x + row;
                let ncol = _y + col;
                let is_valid = isValidBound(puzzle, row, col);
                if (is_valid && isDigit(puzzle[nrow][ncol])) {
                    let {num, key} = getNumber(puzzle, nrow, ncol);
                    nums_found[key] = num
                }
            }
            if(Object.keys(nums_found).length == 2){
                sum += Object.values(nums_found).reduce((agg,v)=>agg*v,1)
            }
        }
    }


    console.log(sum)
}

solve2part(puzzle_input)