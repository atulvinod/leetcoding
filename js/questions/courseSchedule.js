/**
 * https://leetcode.com/problems/course-schedule/description
 * to find if a loop exists in a graph using topological sort
 */

function canFinish(numCourses, prerequisites) {
    if (prerequisites.length === 0) {
        return true;
    }
    // maintain an adjacency list for each node
    const adjList = new Map();

    // maintain an indgree map for each node
    const indegrees = new Map();
    const q = [];

    for (const courses of prerequisites) {
        const neighbours = adjList.get(courses[1]) || [];
        neighbours.push(courses[0]);
        adjList.set(courses[1], neighbours);
        indegrees.set(courses[0], 0);
        indegrees.set(courses[1], 0);
    }

    for (const [key, value] of adjList.entries()) {
        for (const e of value) {
            indegrees.set(e, (indegrees.get(e) || 0) + 1);
        }
    }

    // push all the nodes whose indegree is zero
    for (const [key, value] of indegrees.entries()) {
        if (value === 0) {
            q.push(key);
        }
    }

    let processedElements = 0;
    while (q.length > 0) {
        const value = q.shift();
        processedElements++;

        //reduce the indegree of each neighbour node, if the value becomes
        //zero then add that node to the queue
        for (const i of adjList.get(value) || []) {
            let indeg = indegrees.get(i) || 0;
            if (indeg === 0) continue;

            
            indeg = indeg - 1;
            if (indeg === 0) {
                q.push(i);
            }
            indegrees.set(i, indeg);
        }
    }

    return processedElements === indegrees.size;
}

// Example usage:
const numCourses = 4;
const prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]];
console.log(canFinish(numCourses, prerequisites));