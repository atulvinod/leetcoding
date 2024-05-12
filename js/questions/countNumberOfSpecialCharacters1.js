//https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function (word) {
    const markedAsSpecial = {}
    const visited = {}
    let special = 0
    for (let i = 0; i < word.length; i++) {
        const w = word[i]
        if ((!markedAsSpecial[w] && w.toUpperCase() == w && visited[w.toLowerCase()]) || (!markedAsSpecial[w] && w.toLowerCase() == w && visited[w.toUpperCase()])) {
            special += 1
            markedAsSpecial[w.toUpperCase()] = true
            markedAsSpecial[w.toLowerCase()] = true
        }
        visited[w] = true
    }
    return special
};