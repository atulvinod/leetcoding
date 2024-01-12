/*
Our goal is trying to use two colors to color the graph and see if there are any adjacent nodes having the same color.
Initialize a color[] array for each node. Here are three states for colors[] array:
0: Haven't been colored yet.
1: Blue.
-1: Red.
For each node,

If it hasn't been colored, use a color to color it (eg Blue). Then use the other color to color 
all its adjacent nodes (eg Red) 
, keep going on in a DFS manner in an alternate coloring pattern (Blue -> Red -> Blue -> Red).
If a node is already colored,then check if the current color is the same as
 the color that is going to be used to color it. 
if not, then the graph is not bi-part
 */
function isBipartite(graph) {
    const n = graph.length;
    const colors = new Array(n).fill(0);

    for (let i = 0; i < n; i++) {
        if (colors[i] === 0 && !validColor(graph, colors, 1, i)) {
            return false;
        }
    }
    return true;
}

function validColor(graph, colors, color, node) {
    if (colors[node] !== 0) {
        return colors[node] === color;
    }
    colors[node] = color;

    for (const next of graph[node]) {
        if (!validColor(graph, colors, -color, next)) {
            return false;
        }
    }
    return true;
}

// Example usage:
const graph = [[1, 3], [0, 2], [1, 3], [0, 2]];
console.log(isBipartite(graph));