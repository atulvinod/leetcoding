const array  = require( "./puzzle_input");

let names = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
};

let name_keys = Object.keys(names)

let totalSum = 0;

function isDigit(char) {
    return char >= '0' && char <= '9'
}

let temp =[
    "two1nine"
,"eightwothree"
,"abcone2threexyz"
,"xtwone3four"
,"4nineeightseven2"
,"zoneight234"
,"7pqrstsixteen"
]

array.forEach((str) => {
    let leftDigitIndex = Number.MAX_SAFE_INTEGER, rightDigitIndex = Number.MIN_SAFE_INTEGER, leftNameIndex = Number.MAX_SAFE_INTEGER, rightNameIndex = Number.MIN_SAFE_INTEGER;
    let finalDigits = ''
    for (let i = 0; i < str.length; i++) {
        if (isDigit(str[i])) {
            leftDigitIndex = i;
            break;
        }
    }
    for (let i = str.length; i >= 0; i--) {
        if (isDigit(str[i])) {
            rightDigitIndex = i;
            break;
        }
    }

    let leftStartIndexes = []
    let leftIndexMap = {}

    let rightStartIndexes = []
    let rightIndexMap = {}

    name_keys.forEach(name => {
        let firstIndex = str.indexOf(name);
        let lastIndex = str.lastIndexOf(name)

        if (firstIndex != -1) {
            leftStartIndexes.push(firstIndex)
            leftIndexMap[firstIndex] = name;
        }
        if (lastIndex != -1) {
            rightStartIndexes.push(lastIndex)
            rightIndexMap[lastIndex] = name;
        }
    })

    leftNameIndex = Math.min(...leftStartIndexes);
    rightNameIndex = Math.max(...rightStartIndexes)

    if (  leftNameIndex < leftDigitIndex) {
        let digit = leftIndexMap[leftNameIndex];
        finalDigits += names[digit];
    } else {
        finalDigits += str[leftDigitIndex]
    }

    if (rightNameIndex > rightDigitIndex) {
        let digit = rightIndexMap[rightNameIndex]
        finalDigits += names[digit]
    }else{
        finalDigits += str[rightDigitIndex];
    }
    console.log(str,' ',finalDigits)
    totalSum += Number(finalDigits);
})


console.log('Result ', totalSum);