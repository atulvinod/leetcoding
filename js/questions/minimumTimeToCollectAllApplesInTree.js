/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function(n, edges, hasApple) {
    let result = 0;
    let adjMatrix = {}
    let visited = {};
    for(const [A, B] of edges){
        if(!Array.isArray(adjMatrix[A])){
            adjMatrix[A] = []
        }
        if(!Array.isArray(adjMatrix[B])){
            adjMatrix[B] = []
        }
        adjMatrix[A].push(B)
        adjMatrix[B].push(A)
    }

    /**
     * 
     * @param {Set} visited_set 
     * @param {Number} index 
     * @returns 
     */
    function traverse(visited_set, index){
        if(visited_set.has(index)){
            return;
        }
        visited_set.add(index);
        if(hasApple[index]){
            let visited_upto_now = Array.from(visited_set);
            for(let v of visited_upto_now){
                if(!visited[v] && v != 0){
                    result += 2;
                    visited[v] = true;
                }
            }
        }
        let neighbours = adjMatrix[index];
        for(let n of neighbours){
            if(!visited_set.has(n)){
                traverse(visited_set, n);
                visited_set.delete(n);
            }
        }
    }
    traverse(new Set(), 0);
    return result;
};


minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    ,[false,false,true,false,false,true,false]
    )