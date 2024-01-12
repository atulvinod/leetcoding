
/**
 *  Dijkstra's algorithm to find the shortest paths from a single source vertex to all other vertices in a weighted graph:

Initialization:

Create a priority queue (or a min-heap) to store nodes along with their tentative distances from the source.
Initialize an array distances to store the tentative distances from the source to each vertex. Set all distances to infinity, except for the source vertex, which is set to 0.
Initialize an array visited to keep track of visited vertices.
Priority Queue Initialization:

Enqueue the source node into the priority queue with a priority of 0.
Dijkstra's Main Loop:

While the priority queue is not empty:
Dequeue the node with the smallest tentative distance from the priority queue.
Mark the node as visited.
For each neighbor of the current node:
Calculate the total tentative distance from the source to the neighbor through the current node.
If the calculated distance is less than the current tentative distance for the neighbor, update the tentative distance.
Enqueue the neighbor into the priority queue with the updated tentative distance.
Result:

After the main loop, the distances array contains the shortest distances from the source to all other vertices.
 */
class PriorityQueue {
    constructor() {
        this.nodes = [];
    }

    enqueue(node, priority) {
        this.nodes.push({ node, priority });
        this.nodes.sort((a, b) => a.priority - b.priority);
    }

    dequeue() {
        return this.nodes.shift();
    }

    isEmpty() {
        return this.nodes.length === 0;
    }
}

function dijkstra(graph, source) {
    const distances = {};
    const visited = {};
    const pq = new PriorityQueue();

    // Initialize distances and enqueue the source node with distance 0
    for (let vertex in graph) {
        distances[vertex] = Infinity;
        visited[vertex] = false;
    }
    distances[source] = 0;
    pq.enqueue(source, 0);

    while (!pq.isEmpty()) {
        const { node, priority } = pq.dequeue();

        // Skip if the node is already visited
        if (visited[node]) continue;

        visited[node] = true;

        for (let neighbor in graph[node]) {
            const weight = graph[node][neighbor];
            const totalDistance = distances[node] + weight;

            if (totalDistance < distances[neighbor]) {
                distances[neighbor] = totalDistance;
                pq.enqueue(neighbor, totalDistance);
            }
        }
    }

    return distances;
}

// Example usage:
const graph = {
    A: { B: 1, C: 4 },
    B: { A: 1, C: 2, D: 5 },
    C: { A: 4, B: 2, D: 1 },
    D: { B: 5, C: 1 },
};

const sourceNode = 'A';
const result = dijkstra(graph, sourceNode);
console.log(result);
