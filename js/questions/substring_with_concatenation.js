/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function (s, words) {
    let result = []
    let permutation = []
    solve({}, s, words, permutation, result)
    return [...new Set(result)];
};


function findIndexes(source, find) {
    if (!source) {
        return [];
    }
    if (!find) {
        return source.split('').map(function (_, i) { return i; });
    }
    var result = [];
    var i = 0;
    while (i < source.length) {
        if (source.substring(i, i + find.length) == find) {
            result.push(i);
        }
        i++;
    }
    return result;
}

var solve = function (visited, string, words, permutation, result) {
    if (permutation.length == words.length) {
        let permutationResult = permutation.join('');
        let indexes = findIndexes(string, permutationResult)
        if (indexes.length) {
            result.push(...indexes)
        }
        return;
    }

    for (let i = 0; i < words.length; i++) {
        if (!visited[i]) {
            visited[i] = true
            permutation.push(words[i])
            solve(visited, string, words, permutation, result)
            permutation.pop()
            visited[i] = false;
        }
    }
}

findSubstring("aaa", ["a", "a"])
