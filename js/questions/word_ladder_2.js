var isValid = function (board, x, y) {
    return (x >= 0 && x < board.length && y >= 0 && y < board[0].length)
}

var buildRootAndChildren = function(board){
    let root = {};
    let children = {};
    let vector = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]
    for (let row = 0; row < board.length; row++) {
        for (let col = 0; col < board[0].length; col++) {
            if (!(board[row][col] in root)) {
                root[board[row][col]] = []
            }
            root[board[row][col]].push(`${row},${col}`);
            for (let [_x, _y] of vector) {
                if (isValid(board, _x + row, _y + col)) {
                    if (!(`${row},${col}` in children)) {
                        children[`${row},${col}`] = {}
                    }
                    if (!(board[row + _x][col + _y] in children[`${row},${col}`])) {
                        children[`${row},${col}`][board[row + _x][col + _y]] = []
                    }
                    children[`${row},${col}`][board[row + _x][col + _y]].push(`${row + _x},${col + _y}`)
                }
            }
        }
    }

    return {root, children}
}

var findWordInTrie = function(currentNode, trie_children, word, visited){
    const children = trie_children[currentNode] ?? {};
    visited[currentNode] = true;
    if(word.length == 1){
        if (word in children){
            for(let n of children[word]){
                if(!visited[n]){
                    return true;
                }
            }
        }
        return false
    }

    const nextNode = trie_children[currentNode][word[0]];
    if(!nextNode){
        visited[currentNode] = false
        return false;
    }

    for(let n of nextNode){
        if(!visited[n]){
            const nextResult = findWordInTrie(n, trie_children, word.slice(1), visited)
            if(nextResult) {
                visited[currentNode] = false
                return true;
            }
        }
    }
    visited[currentNode] = false
    return false;

}

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function (board, words) {
    const {root, children} = buildRootAndChildren(board);
    const result = []
    for(const w of words){
        if(w.length > (board.length*board[0].length)){
            continue;
        }
        if(w[0] in root){
            for(let nodes of root[w[0]]){
                if(w.length == 1){
                    result.push(w);
                    break;
                }else{
                    const isInBoard = findWordInTrie(nodes, children, w.slice(1), {})
                    if(isInBoard){
                        result.push(w);
                        break;
                    }
                }
                
            }
        }
    }
    return result;
};

// findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],['oath','pea','eat','rain'])
// findWords([['a']],['ab'])
/// findWords([["a","b"],["a","a"]],['bab'])
findWords([["a","b","c"],["a","e","d"],["a","f","g"]]
,['eaabcdgfa'])