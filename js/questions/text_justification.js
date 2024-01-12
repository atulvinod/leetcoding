var buildString = function(strings, maxWidth,curWordLength){
    let totalSpace = maxWidth - curWordLength;
    let finalString = '';
    if(strings.length == 1){
        finalString = strings[0]+ ' '.repeat(maxWidth-curWordLength)
        return finalString;
    }

    let i = 0;
    while(totalSpace--){
        strings[i] += ' ';
        i = (i+1)%(strings.length-1)
    }
    return strings.join('');
}

var buildFinalString = function(strings, maxWidth){
    let finalString = strings.join(' ')
    if(finalString.length < maxWidth){
        finalString += ' '.repeat(maxWidth - finalString.length);
    }
    return finalString;
}

/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function (words, maxWidth) {
    const result = []
    let temp = []
    let curWordLength = 0
    let wordSpace = 0;
    for (let w of words) {
        let isLimitValid = curWordLength + wordSpace + w.length <= maxWidth;
        if (isLimitValid) {
            curWordLength += w.length;
            wordSpace++;
            temp.push(w)
        } else {
            const finalString = buildString(temp, maxWidth, curWordLength)
            result.push(finalString)
            curWordLength = w.length;
            wordSpace = 1;
            temp = [w]
        }
    }
    if(temp.length){
        const string = buildFinalString(temp, maxWidth)
        result.push(string)
    }

    return result;
};

fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20)