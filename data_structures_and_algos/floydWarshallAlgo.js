/**
 * The Floyd-Warshall algorithm is used for finding the shortest paths between all pairs of vertices in a weighted graph. Here are the step-by-step 
 * instructions for implementing the Floyd-Warshall algorithm:

Initialization:

Create a 2D array dist of size V x V (where V is the number of vertices in the graph) to store the shortest distances between all pairs of vertices.
Initialize the dist array such that dist[i][j] is the weight of the edge between vertices i and j if there is an edge, and dist[i][j] = INF (or a very large number) if there is no direct edge between i and j.
Initialize the diagonal elements dist[i][i] = 0 for all vertices.
Update the Distances:

For each vertex k from 0 to V-1, iterate over all pairs of vertices i and j.
Update dist[i][j] to be the minimum of the current dist[i][j] and the sum of distances from i to k and from k to j, i.e., dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]).
Result:

After the completion of the above steps, the dist array will contain the shortest distances between all pairs of vertices.
 */
function shortest_distance(matrix) {
    for (let current = 0; current < matrix.length; current++) {
        for (let row = 0; row < matrix.length; row++) {
            for (let col = 0; col < matrix.length; col++) {
                if (row == current || col == current) {
                    continue;
                }
                let d = (matrix[row][col]);
                let a = (matrix[row][current]);
                let b = (matrix[current][col]);
                // -1 indicates that there is no edge aka Infinity distance, the addition will result in
                // Infinite distance
                if (a == -1 || b == -1) {
                    continue;
                }
                matrix[row][col] = Math.min(d == -1 ? Number.MAX_SAFE_INTEGER : d, a + b);
            }
        }
    }
}