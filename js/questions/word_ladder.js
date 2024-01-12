var isValidEdge = function (currentWord, nextWord) {
    let diff = 0
    for (let i = 0; i < currentWord.length; i++) {
        if (currentWord[i] != nextWord[i]) {
            diff++;
            if (diff > 1) {
                return false;
            }
        }
    }
    return diff == 1;
}

var getAdjList = function (wordList) {
    let adjList = {}
    for (let i = 0; i < wordList.length; i++) {
        for (let j = 0; j < wordList.length; j++) {
            if (isValidEdge(wordList[i], wordList[j])) {
                if (!(wordList[i] in adjList)) {
                    adjList[wordList[i]] = []
                }
                adjList[wordList[i]].push(wordList[j])
            }
        }
    }

    return adjList;
}

var getWeights = function (wordList) {
    return wordList.reduce((agg, v) => {
        agg[v] = Number.MAX_SAFE_INTEGER;
        return agg;
    }, {})
}

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function (beginWord, endWord, wordList) {
    wordList.unshift(beginWord);
    let adjList = getAdjList(wordList);
    let weights = getWeights(wordList);
    let visited = new Array(wordList.length);
    let queue = []
    queue.push(beginWord);
    weights[beginWord] = 0;

    while (queue.length) {
        let currentNode = queue.shift();
        if (visited[currentNode]) {
            continue;
        }
        visited[currentNode] = true;
        let neighbors = adjList[currentNode];
        for (let neighbor of neighbors) {
            if(!visited[neighbor]){
                queue.push(neighbor);
            }
            let neighborCurrentDistance = weights[neighbor];
            let neighborDistanceFromCurrent = weights[currentNode] + 1;
            if (neighborDistanceFromCurrent < neighborCurrentDistance) {
                weights[neighbor] = neighborDistanceFromCurrent;
            }
        }
    }

    return weights[endWord] == undefined || weights[endWord] == Number.MAX_SAFE_INTEGER ? 0 : weights[endWord]
};

ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"])