/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function (word) {
    const allCharacters = new Set()
    const lowerCaseLetterIndex = {}
    const upperCaseLetterIndex = {}
    for (let i = 0; i < word.length; i++) {
        let w = word[i]
        allCharacters.add(w)
        if (w.toLowerCase() == w && (!(w in lowerCaseLetterIndex) || i > lowerCaseLetterIndex[w])) {
            lowerCaseLetterIndex[w] = i
        }
        if (w.toUpperCase() == w && (!(w in upperCaseLetterIndex) || i < upperCaseLetterIndex[w])) {
            upperCaseLetterIndex[w] = i
        }
    }
    let result = 0;
    const wordArr = Array.from(allCharacters)
    const visited = {}
    for (let i = 0; i < wordArr.length; i++) {
        const w = wordArr[i]
        const upperCase = w.toUpperCase()
        const lowerCase = w.toLowerCase()
        if (!visited[lowerCase] && !visited[upperCase]) {
            if ((lowerCase in lowerCaseLetterIndex && upperCase in upperCaseLetterIndex) && (lowerCaseLetterIndex[lowerCase] < upperCaseLetterIndex[upperCase])) {
                result += 1
                visited[lowerCase] = true
                visited[upperCase] = true
            }
        }
    }

    return result
};