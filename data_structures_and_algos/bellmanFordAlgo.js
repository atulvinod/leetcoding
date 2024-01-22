/**
 * The Bellman-Ford algorithm is used to find the shortest paths from a single source vertex to all other vertices in a weighted graph, even if the graph contains negative weight edges (as long as there are no negative cycles)
 * Initialization:

Create an array dist of size V (where V is the number of vertices in the graph) to store the shortest distances from the source vertex to each vertex.
Initialize dist such that dist[source] = 0 and dist[v] = INF for all other vertices.
Relaxation:

Repeat the relaxation step for each edge in the graph, a total of V-1 times.
For each edge (u, v) with weight w, if dist[u] + w < dist[v], update dist[v] to dist[u] + w.
The relaxation step aims to find shorter paths.
Check for Negative Cycles:

After V-1 iterations, if any relaxation step further reduces the distance, it means there is a negative cycle in the graph.
In the presence of a negative cycle, the algorithm cannot guarantee correct results.
Result:

The dist array contains the shortest distances from the source vertex to all other vertices.
 * 
 * 
 */

function bfs(adjList, source, distances) {
    // Flag to track if any distance has been updated during BFS
    let hasAnyDistanceUpdated = false;

    // Initialize the queue with the source vertex
    let queue = [source];

    // Perform BFS
    while (queue.length > 0) {
        let size = queue.length;

        // Process all vertices at the current level
        while (size > 0) {
            // Dequeue a vertex
            let vertex = queue.shift();

            // Get neighbors of the current vertex from the adjacency list
            let neighbours = adjList[vertex] || [];

            // Iterate over neighbors
            for (let n of neighbours) {
                let dest = n[0];
                let wt = n[1];

                // Relaxation step: update distance if a shorter path is found
                if (distances[vertex] + wt < distances[dest]) {
                    distances[dest] = distances[vertex] + wt;
                    hasAnyDistanceUpdated = true;
                }

                // Enqueue the destination vertex for the next level
                queue.push(dest);
            }

            // Decrease the size for the next iteration
            size--;
        }
    }

    // Return whether any distance has been updated during BFS
    return hasAnyDistanceUpdated;
}

function bellmanFord(V, edges, source) {
    // Initialize distances array with max values
    let distances = new Array(V).fill(1e8);

    // Set the source vertex distance to 0
    distances[source] = 0;

    // Create an adjacency list from the given edges
    let adjList = {};
    for (let edge of edges) {
        let s = edge[0];
        let d = edge[1];
        let w = edge[2];
        let list = adjList[s] || [];
        list.push([d, w]);
        adjList[s] = list;
    }

    // Number of iterations
    let iterations = 0;

    // Perform Bellman-Ford iterations
    while (true) {
        // Check if any distance has been updated during BFS
        let hasAnyDistanceUpdated = bfs(adjList, source, distances);

        // If distances are not updated in the current iteration, break the loop
        if (!hasAnyDistanceUpdated) {
            break;
        }

        // Increment the iteration count
        iterations++;

        // If the number of iterations exceeds the number of vertices, there is a negative cycle
        // if there is a negative cycle, then there is a cycle and bellman ford cannot be used to
        // find distances
        if (iterations >= V) {
            return [-1];
        }
    }

    // Return the final distances
    return distances;
}
